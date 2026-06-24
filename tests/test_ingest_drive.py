"""Testes para integração Google Drive (ingest_drive.py).

Todos os testes usam mocks — não requerem credentials.json nem acesso à internet.
"""
import json
import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch
import sys
import io

import pytest
import frontmatter

sys.path.insert(0, str(Path(__file__).parent.parent))


FAKE_FILES = [
    {
        "id": "file_abc123",
        "name": "Apresentação Métodos.pptx",
        "mimeType": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "modifiedTime": "2026-06-15T10:00:00.000Z",
    },
    {
        "id": "file_def456",
        "name": "Relatório Final.pdf",
        "mimeType": "application/pdf",
        "modifiedTime": "2026-06-16T14:30:00.000Z",
    },
    {
        "id": "file_ghi789",
        "name": "Planilha Custos",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "modifiedTime": "2026-06-17T09:00:00.000Z",
    },
]

UNSUPPORTED_FILE = {
    "id": "file_unsupported",
    "name": "Imagem.png",
    "mimeType": "image/png",
    "modifiedTime": "2026-06-17T12:00:00.000Z",
}


def _make_mock_service(files: list[dict], file_content: bytes = b"fake content"):
    """Cria um mock do serviço Google Drive API."""
    service = MagicMock()

    list_result = {"files": files, "nextPageToken": None}
    service.files().list().execute.return_value = list_result
    service.files().list.return_value.execute.return_value = list_result

    def mock_get_media(fileId):
        mock_request = MagicMock()
        mock_request.execute.return_value = file_content
        mock_request.uri = f"https://drive.google.com/file/{fileId}"
        mock_request.headers = {}
        return mock_request

    def mock_export_media(fileId, mimeType):
        mock_request = MagicMock()
        mock_request.execute.return_value = file_content
        mock_request.uri = f"https://drive.google.com/export/{fileId}"
        mock_request.headers = {}
        return mock_request

    service.files().get_media = mock_get_media
    service.files().export_media = mock_export_media

    return service


@pytest.fixture
def kb_bundle(tmp_path):
    """Cria um bundle OKF mínimo para testes."""
    kb = tmp_path / "kb"
    kb.mkdir()

    log_post = frontmatter.Post(
        "# Log\n\n- **2026-06-17** — Bundle inicial.",
        type="Log",
        title="Histórico de mudanças da KB",
        description="Registro cronológico.",
        resource="",
        tags=["log"],
        timestamp="2026-06-17T12:00:00Z",
    )
    (kb / "log.md").write_text(frontmatter.dumps(log_post), encoding="utf-8")

    out = kb / "drive-import"
    out.mkdir()
    return kb, out


class TestListFiles:
    def test_list_returns_all_files(self):
        from ingest_drive import list_files

        service = _make_mock_service(FAKE_FILES)
        result = list_files(service, "folder_id_test")
        assert len(result) == 3

    def test_list_empty_folder(self):
        from ingest_drive import list_files

        service = _make_mock_service([])
        result = list_files(service, "folder_id_empty")
        assert result == []


class TestDownloadFile:
    def test_download_pdf(self, tmp_path):
        from ingest_drive import download_file

        service = _make_mock_service([], b"PDF fake content")
        pdf_file = FAKE_FILES[1]

        with patch("ingest_drive.MediaIoBaseDownload") as mock_dl:
            mock_instance = MagicMock()
            mock_instance.next_chunk.return_value = (None, True)
            mock_dl.return_value = mock_instance

            result = download_file(service, pdf_file, tmp_path)

        assert result is not None
        assert result.suffix == ".pdf"
        assert result.exists()

    def test_download_google_sheet_exports_csv(self, tmp_path):
        from ingest_drive import download_file

        service = _make_mock_service([], b"col1,col2\nval1,val2")
        sheet_file = FAKE_FILES[2]

        with patch("ingest_drive.MediaIoBaseDownload") as mock_dl:
            mock_instance = MagicMock()
            mock_instance.next_chunk.return_value = (None, True)
            mock_dl.return_value = mock_instance

            result = download_file(service, sheet_file, tmp_path)

        assert result is not None
        assert result.suffix == ".csv"

    def test_download_unsupported_returns_none(self, tmp_path):
        from ingest_drive import download_file

        service = _make_mock_service([])
        result = download_file(service, UNSUPPORTED_FILE, tmp_path)
        assert result is None


class TestFilterChangedFiles:
    def test_all_new_when_no_state(self):
        from ingest_drive import filter_changed_files

        changed = filter_changed_files(FAKE_FILES, {})
        assert len(changed) == 3

    def test_filters_unchanged(self):
        from ingest_drive import filter_changed_files

        state = {
            "file_abc123": {"modifiedTime": "2026-06-15T10:00:00.000Z"},
            "file_def456": {"modifiedTime": "2026-06-16T14:30:00.000Z"},
        }
        changed = filter_changed_files(FAKE_FILES, state)
        assert len(changed) == 1
        assert changed[0]["id"] == "file_ghi789"

    def test_detects_modification(self):
        from ingest_drive import filter_changed_files

        state = {
            "file_abc123": {"modifiedTime": "2026-06-14T00:00:00.000Z"},
        }
        changed = filter_changed_files(FAKE_FILES, state)
        ids = [f["id"] for f in changed]
        assert "file_abc123" in ids


class TestSyncState:
    def test_save_and_load(self, tmp_path):
        from ingest_drive import save_sync_state, load_sync_state

        state_file = tmp_path / ".drive-sync.json"
        state = {
            "file_abc123": {
                "name": "test.pdf",
                "mimeType": "application/pdf",
                "modifiedTime": "2026-06-17T12:00:00Z",
            }
        }
        save_sync_state(state, state_file)
        loaded = load_sync_state(state_file)
        assert loaded == state

    def test_load_missing_file(self, tmp_path):
        from ingest_drive import load_sync_state

        state_file = tmp_path / "nonexistent.json"
        assert load_sync_state(state_file) == {}


class TestResourceTracking:
    def test_resource_id_format(self):
        from ingest_drive import _resource_id

        assert _resource_id("abc123") == "drive://abc123"

    def test_find_existing_by_resource(self, tmp_path):
        from ingest_drive import _find_existing_by_resource

        kb = tmp_path / "kb"
        kb.mkdir()

        post = frontmatter.Post(
            "# Test",
            type="Conceito",
            title="Test",
            resource="drive://file_abc123",
            tags=[],
            timestamp="2026-06-17T12:00:00Z",
        )
        (kb / "test.md").write_text(frontmatter.dumps(post), encoding="utf-8")

        found = _find_existing_by_resource(kb, "drive://file_abc123")
        assert found is not None
        assert found.name == "test.md"

    def test_find_existing_returns_none_when_missing(self, tmp_path):
        from ingest_drive import _find_existing_by_resource

        kb = tmp_path / "kb"
        kb.mkdir()
        assert _find_existing_by_resource(kb, "drive://nonexistent") is None


class TestSyncDrive:
    def test_full_sync_creates_concepts(self, kb_bundle, tmp_path):
        """Sincronização completa baixa e converte arquivos."""
        kb, out = kb_bundle
        state_file = tmp_path / ".drive-sync.json"

        md_content = textwrap.dedent("""\
        # Relatório Final

        Conteúdo do relatório sobre o projeto Trituradora.
        """).encode("utf-8")

        md_file = {
            "id": "file_md001",
            "name": "relatorio.md",
            "mimeType": "text/markdown",
            "modifiedTime": "2026-06-16T14:30:00.000Z",
        }

        service = _make_mock_service([md_file], md_content)

        with patch("ingest_drive.MediaIoBaseDownload") as mock_dl:
            mock_instance = MagicMock()
            mock_instance.next_chunk.return_value = (None, True)
            mock_dl.return_value = mock_instance

            with patch("ingest_drive.list_files", return_value=[md_file]):
                from ingest_drive import sync_drive

                result = sync_drive(
                    folder_id="test_folder",
                    out=out,
                    service=service,
                    state_file=state_file,
                )

        assert len(result) > 0
        assert state_file.exists()

        state = json.loads(state_file.read_text())
        assert "file_md001" in state

    def test_incremental_skips_unchanged(self, kb_bundle, tmp_path):
        """Sincronização incremental ignora arquivos não modificados."""
        kb, out = kb_bundle
        state_file = tmp_path / ".drive-sync.json"

        state = {
            "file_def456": {
                "name": "Relatório Final.pdf",
                "mimeType": "application/pdf",
                "modifiedTime": "2026-06-16T14:30:00.000Z",
            }
        }
        state_file.write_text(json.dumps(state))

        service = _make_mock_service([FAKE_FILES[1]])

        with patch("ingest_drive.list_files", return_value=[FAKE_FILES[1]]):
            from ingest_drive import sync_drive

            result = sync_drive(
                folder_id="test_folder",
                out=out,
                service=service,
                state_file=state_file,
                incremental=True,
            )

        assert result == []

    def test_sync_empty_folder(self, kb_bundle, tmp_path):
        """Pasta vazia no Drive não gera conceitos."""
        kb, out = kb_bundle
        state_file = tmp_path / ".drive-sync.json"

        service = _make_mock_service([])

        with patch("ingest_drive.list_files", return_value=[]):
            from ingest_drive import sync_drive

            result = sync_drive(
                folder_id="empty_folder",
                out=out,
                service=service,
                state_file=state_file,
            )

        assert result == []

    def test_sync_updates_log(self, kb_bundle, tmp_path):
        """Sincronização registra entrada no log.md."""
        kb, out = kb_bundle
        state_file = tmp_path / ".drive-sync.json"

        md_file = {
            "id": "file_log001",
            "name": "teste.md",
            "mimeType": "text/markdown",
            "modifiedTime": "2026-06-17T10:00:00.000Z",
        }
        md_content = b"# Teste\n\nConteudo de teste."
        service = _make_mock_service([md_file], md_content)

        with patch("ingest_drive.MediaIoBaseDownload") as mock_dl:
            mock_instance = MagicMock()
            mock_instance.next_chunk.return_value = (None, True)
            mock_dl.return_value = mock_instance

            with patch("ingest_drive.list_files", return_value=[md_file]):
                from ingest_drive import sync_drive

                sync_drive(
                    folder_id="test_folder",
                    out=out,
                    service=service,
                    state_file=state_file,
                )

        log_content = (kb / "log.md").read_text()
        assert "Google Drive" in log_content


class TestSafeStem:
    def test_preserves_name_with_internal_dots(self):
        from ingest_drive import _safe_stem

        assert _safe_stem("SDE 2026.2 - GERAL") == "SDE 2026.2 - GERAL"

    def test_strips_known_extension(self):
        from ingest_drive import _safe_stem

        assert _safe_stem("Relatório Final.pdf") == "Relatório Final"
        assert _safe_stem("planilha.csv") == "planilha"

    def test_preserves_name_without_extension(self):
        from ingest_drive import _safe_stem

        assert _safe_stem("Meu Documento") == "Meu Documento"

    def test_google_sheets_names_unique(self, tmp_path):
        """Três Google Sheets com nomes similares devem gerar arquivos distintos."""
        from ingest_drive import download_file

        names = [
            "SDE 2026.2 - EXTRUSORA (21h)",
            "SDE 2026.2 - GERAL",
            "SDE 2026.2 - TRITURADORA (19h)",
        ]
        paths = set()
        for i, name in enumerate(names):
            file_info = {
                "id": f"sheet_{i}",
                "name": name,
                "mimeType": "application/vnd.google-apps.spreadsheet",
                "modifiedTime": "2026-06-17T09:00:00.000Z",
            }
            service = _make_mock_service([], b"col1,col2\nval1,val2")

            with patch("ingest_drive.MediaIoBaseDownload") as mock_dl:
                mock_instance = MagicMock()
                mock_instance.next_chunk.return_value = (None, True)
                mock_dl.return_value = mock_instance

                result = download_file(service, file_info, tmp_path)
                paths.add(result.name)

        assert len(paths) == 3


class TestRecursive:
    def test_list_folders(self):
        from ingest_drive import list_folders

        folders = [
            {
                "id": "folder_sub1",
                "name": "Subpasta A",
                "mimeType": "application/vnd.google-apps.folder",
                "modifiedTime": "2026-06-17T12:00:00.000Z",
            }
        ]
        service = _make_mock_service(folders)
        result = list_folders(service, "parent_folder")
        assert len(result) == 1
        assert result[0]["name"] == "Subpasta A"

    def test_list_files_recursive_flat(self):
        """Pasta sem subpastas retorna arquivos com subfolder vazio."""
        from ingest_drive import list_files_recursive

        service = MagicMock()

        def mock_list(q, fields, pageToken, orderBy):
            mock_resp = MagicMock()
            if "mimeType != " in q:
                mock_resp.execute.return_value = {
                    "files": [FAKE_FILES[0]],
                    "nextPageToken": None,
                }
            else:
                mock_resp.execute.return_value = {
                    "files": [],
                    "nextPageToken": None,
                }
            return mock_resp

        service.files().list = mock_list

        result = list_files_recursive(service, "root_folder")
        assert len(result) == 1
        assert result[0]["subfolder"] == ""

    def test_list_files_recursive_with_subfolder(self):
        """Pasta com subpasta retorna arquivos com subfolder preenchido."""
        from ingest_drive import list_files_recursive

        subfolder = {
            "id": "folder_sub1",
            "name": "Documentos Técnicos",
            "mimeType": "application/vnd.google-apps.folder",
            "modifiedTime": "2026-06-17T12:00:00.000Z",
        }
        sub_file = {
            "id": "file_in_sub",
            "name": "specs.md",
            "mimeType": "text/markdown",
            "modifiedTime": "2026-06-18T10:00:00.000Z",
        }

        service = MagicMock()
        call_count = {"n": 0}

        def mock_list(q, fields, pageToken, orderBy):
            mock_resp = MagicMock()
            call_count["n"] += 1

            if "'root_folder'" in q and "mimeType != " in q:
                mock_resp.execute.return_value = {
                    "files": [FAKE_FILES[0]],
                    "nextPageToken": None,
                }
            elif "'root_folder'" in q and "mimeType = " in q:
                mock_resp.execute.return_value = {
                    "files": [subfolder],
                    "nextPageToken": None,
                }
            elif "'folder_sub1'" in q and "mimeType != " in q:
                mock_resp.execute.return_value = {
                    "files": [sub_file],
                    "nextPageToken": None,
                }
            else:
                mock_resp.execute.return_value = {
                    "files": [],
                    "nextPageToken": None,
                }
            return mock_resp

        service.files().list = mock_list

        result = list_files_recursive(service, "root_folder")
        assert len(result) == 2

        root_files = [f for f in result if f["subfolder"] == ""]
        sub_files = [f for f in result if f["subfolder"] != ""]
        assert len(root_files) == 1
        assert len(sub_files) == 1
        assert sub_files[0]["subfolder"] == "documentos-técnicos"
        assert sub_files[0]["name"] == "specs.md"

    def test_sync_recursive_creates_subdirs(self, kb_bundle, tmp_path):
        """Sync recursivo cria subpastas correspondentes no bundle."""
        kb, out = kb_bundle
        state_file = tmp_path / ".drive-sync.json"

        root_file = {
            "id": "file_root",
            "name": "readme.md",
            "mimeType": "text/markdown",
            "modifiedTime": "2026-06-17T10:00:00.000Z",
            "subfolder": "",
        }
        sub_file = {
            "id": "file_sub",
            "name": "detalhe.md",
            "mimeType": "text/markdown",
            "modifiedTime": "2026-06-17T11:00:00.000Z",
            "subfolder": "metodos",
        }

        service = _make_mock_service([], b"# Conteudo\n\nTexto de teste.")

        with patch("ingest_drive.list_files_recursive", return_value=[root_file, sub_file]):
            with patch("ingest_drive.MediaIoBaseDownload") as mock_dl:
                mock_instance = MagicMock()
                mock_instance.next_chunk.return_value = (None, True)
                mock_dl.return_value = mock_instance

                from ingest_drive import sync_drive

                result = sync_drive(
                    folder_id="test_folder",
                    out=out,
                    service=service,
                    state_file=state_file,
                    recursive=True,
                )

        assert len(result) > 0
        assert (out / "metodos").is_dir()


class TestExportMimes:
    def test_google_docs_export_mapping(self):
        from ingest_drive import EXPORT_MIMES

        assert "application/vnd.google-apps.spreadsheet" in EXPORT_MIMES
        assert "application/vnd.google-apps.document" in EXPORT_MIMES
        assert "application/vnd.google-apps.presentation" in EXPORT_MIMES

    def test_sheet_exports_to_csv(self):
        from ingest_drive import EXPORT_MIMES

        mime, ext = EXPORT_MIMES["application/vnd.google-apps.spreadsheet"]
        assert ext == ".csv"
        assert "csv" in mime

    def test_gdoc_exports_to_docx(self):
        from ingest_drive import EXPORT_MIMES

        mime, ext = EXPORT_MIMES["application/vnd.google-apps.document"]
        assert ext == ".docx"

    def test_gslides_exports_to_pptx(self):
        from ingest_drive import EXPORT_MIMES

        mime, ext = EXPORT_MIMES["application/vnd.google-apps.presentation"]
        assert ext == ".pptx"
