"""Integração Google Drive: sincroniza arquivos de uma pasta do Drive para o bundle OKF.

Uso:
    python ingest_drive.py --folder-id <FOLDER_ID> [--out kb/<subpasta>] [--type <Tipo>]
    python ingest_drive.py --folder-id <FOLDER_ID> --incremental

Requer:
    - credentials.json (OAuth 2.0 do Google Cloud Console)
    - google-api-python-client, google-auth-oauthlib
"""
import argparse
import json
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload
except ImportError:
    print(
        "ERRO: instale as dependências do Google Drive:\n"
        "  pip install google-api-python-client google-auth-oauthlib"
    )
    sys.exit(2)

import io

import frontmatter

from ingest import ingest, _slug, _update_log

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

CREDENTIALS_FILE = Path(__file__).parent / "credentials.json"
TOKEN_FILE = Path(__file__).parent / "token.json"
SYNC_STATE_FILE = Path(__file__).parent / ".drive-sync.json"

EXPORT_MIMES = {
    "application/vnd.google-apps.spreadsheet": (
        "text/csv",
        ".csv",
    ),
    "application/vnd.google-apps.document": (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".docx",
    ),
    "application/vnd.google-apps.presentation": (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".pptx",
    ),
}

SUPPORTED_MIMES = {
    "application/pdf": ".pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": ".pptx",
    "text/csv": ".csv",
    "text/plain": ".txt",
    "text/markdown": ".md",
}

KB_ROOT = Path(__file__).parent / "kb"


def authenticate(credentials_file: Path = CREDENTIALS_FILE,
                 token_file: Path = TOKEN_FILE) -> Credentials:
    """Autentica via OAuth 2.0 com cache de token."""
    creds = None

    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not credentials_file.exists():
                print(
                    f"ERRO: '{credentials_file}' não encontrado.\n"
                    "Crie um projeto no Google Cloud Console, habilite a Google Drive API,\n"
                    "gere credenciais OAuth 2.0 e salve como 'credentials.json'."
                )
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_file), SCOPES
            )
            creds = flow.run_local_server(port=0)

        token_file.write_text(creds.to_json())

    return creds


def build_drive_service(creds: Credentials):
    """Cria o serviço da Google Drive API v3."""
    return build("drive", "v3", credentials=creds)


def list_files(service, folder_id: str) -> list[dict]:
    """Lista todos os arquivos (não-pastas) de uma pasta do Drive.

    Retorna lista de dicts com id, name, mimeType, modifiedTime.
    """
    results = []
    page_token = None

    while True:
        response = service.files().list(
            q=f"'{folder_id}' in parents and trashed = false and mimeType != 'application/vnd.google-apps.folder'",
            fields="nextPageToken, files(id, name, mimeType, modifiedTime)",
            pageToken=page_token,
            orderBy="name",
        ).execute()

        results.extend(response.get("files", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            break

    return results


def download_file(service, file_info: dict, dest_dir: Path) -> Path | None:
    """Baixa um arquivo do Drive para dest_dir. Exporta Google Docs nativos."""
    mime = file_info["mimeType"]
    name = file_info["name"]
    file_id = file_info["id"]

    if mime in EXPORT_MIMES:
        export_mime, ext = EXPORT_MIMES[mime]
        dest = dest_dir / f"{Path(name).stem}{ext}"
        request = service.files().export_media(fileId=file_id, mimeType=export_mime)
    elif mime in SUPPORTED_MIMES:
        ext = SUPPORTED_MIMES[mime]
        stem = Path(name).stem
        dest = dest_dir / f"{stem}{ext}"
        request = service.files().get_media(fileId=file_id)
    else:
        print(f"  IGNORADO: '{name}' (tipo '{mime}' não suportado)")
        return None

    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()

    dest.write_bytes(buffer.getvalue())
    return dest


def load_sync_state(state_file: Path = SYNC_STATE_FILE) -> dict:
    """Carrega o estado da última sincronização."""
    if state_file.exists():
        return json.loads(state_file.read_text(encoding="utf-8"))
    return {}


def save_sync_state(state: dict, state_file: Path = SYNC_STATE_FILE) -> None:
    """Persiste o estado da sincronização."""
    state_file.write_text(
        json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def _resource_id(file_id: str) -> str:
    """Gera o identificador de recurso para rastreamento de idempotência."""
    return f"drive://{file_id}"


def _find_existing_by_resource(kb_dir: Path, resource: str) -> Path | None:
    """Busca um arquivo OKF existente pelo campo resource no frontmatter."""
    for md_path in kb_dir.glob("**/*.md"):
        try:
            post = frontmatter.load(md_path)
            if post.get("resource", "") == resource:
                return md_path
        except Exception:
            continue
    return None


def filter_changed_files(
    files: list[dict], sync_state: dict
) -> list[dict]:
    """Filtra apenas arquivos novos ou modificados desde a última sincronização."""
    changed = []
    for f in files:
        file_id = f["id"]
        modified = f["modifiedTime"]
        prev = sync_state.get(file_id, {}).get("modifiedTime")
        if prev != modified:
            changed.append(f)
    return changed


def sync_drive(
    folder_id: str,
    out: Path,
    tipo: str = "Conceito",
    incremental: bool = False,
    service=None,
    credentials_file: Path = CREDENTIALS_FILE,
    token_file: Path = TOKEN_FILE,
    state_file: Path = SYNC_STATE_FILE,
) -> list[Path]:
    """Sincroniza uma pasta do Google Drive para o bundle OKF.

    Args:
        folder_id: ID da pasta no Google Drive.
        out: Diretório de saída dentro do bundle (ex: kb/drive-import).
        tipo: Tipo OKF dos conceitos gerados.
        incremental: Se True, sincroniza apenas arquivos modificados.
        service: Serviço do Drive (para injeção em testes).
        credentials_file: Caminho para credentials.json.
        token_file: Caminho para token.json.
        state_file: Caminho para .drive-sync.json.

    Returns:
        Lista de Paths dos conceitos gerados/atualizados.
    """
    if service is None:
        creds = authenticate(credentials_file, token_file)
        service = build_drive_service(creds)

    print(f"Listando arquivos da pasta '{folder_id}'...")
    all_files = list_files(service, folder_id)
    print(f"  {len(all_files)} arquivo(s) encontrado(s).")

    if not all_files:
        print("Nenhum arquivo para sincronizar.")
        return []

    sync_state = load_sync_state(state_file)

    if incremental:
        files = filter_changed_files(all_files, sync_state)
        print(f"  {len(files)} arquivo(s) novo(s) ou modificado(s).")
        if not files:
            print("Tudo sincronizado — nenhuma alteração detectada.")
            return []
    else:
        files = all_files

    out.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="drive-sync-") as tmp:
        tmp_dir = Path(tmp)
        downloaded = []

        for f in files:
            print(f"  Baixando: {f['name']}...")
            dest = download_file(service, f, tmp_dir)
            if dest:
                downloaded.append((f, dest))

        if not downloaded:
            print("Nenhum arquivo suportado para converter.")
            return []

        for f, local_path in downloaded:
            resource = _resource_id(f["id"])
            existing = _find_existing_by_resource(out, resource)
            if existing and existing.exists():
                post = frontmatter.load(existing)
                post["resource"] = resource
                post["timestamp"] = datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                )
                existing.write_text(
                    frontmatter.dumps(post), encoding="utf-8"
                )

        generated = ingest(tmp_dir, out, tipo)

        for f, local_path in downloaded:
            resource = _resource_id(f["id"])
            slug = _slug(local_path.name)
            concept_path = out / f"{slug}.md"
            if concept_path.exists():
                post = frontmatter.load(concept_path)
                post["resource"] = resource
                concept_path.write_text(
                    frontmatter.dumps(post), encoding="utf-8"
                )

        for f in files:
            sync_state[f["id"]] = {
                "name": f["name"],
                "mimeType": f["mimeType"],
                "modifiedTime": f["modifiedTime"],
            }
        save_sync_state(sync_state, state_file)

    kb_root = out.parent
    while not (kb_root / "log.md").exists() and kb_root != kb_root.parent:
        kb_root = kb_root.parent

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    mode = "incremental" if incremental else "completa"
    _update_log(
        kb_root,
        f"Sincronização {mode} do Google Drive (pasta `{folder_id}`): "
        f"{len(generated)} conceito(s) sincronizado(s) em `{now}`.",
    )

    print(f"\nSincronização concluída: {len(generated)} conceito(s).")
    return generated


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sincroniza arquivos do Google Drive para o bundle OKF."
    )
    parser.add_argument(
        "--folder-id",
        required=True,
        help="ID da pasta no Google Drive.",
    )
    parser.add_argument(
        "--out",
        default="kb/drive-import",
        help="Subpasta de saída no bundle (padrão: kb/drive-import).",
    )
    parser.add_argument(
        "--type",
        default="Conceito",
        dest="tipo",
        help="Tipo OKF dos conceitos gerados (padrão: Conceito).",
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        help="Sincroniza apenas arquivos novos ou modificados.",
    )
    args = parser.parse_args()

    sync_drive(
        folder_id=args.folder_id,
        out=Path(args.out),
        tipo=args.tipo,
        incremental=args.incremental,
    )


if __name__ == "__main__":
    main()
