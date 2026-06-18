"""Índice de embeddings para busca semântica no bundle OKF.

Uso:
    python embeddings.py              # full reindex
    python embeddings.py --update     # incremental (apenas novos/modificados)
    python embeddings.py --model paraphrase-multilingual-MiniLM-L12-v2  # modelo customizado
"""
import hashlib
import json
import sys
from pathlib import Path

try:
    import frontmatter
except ImportError:
    print("ERRO: instale python-frontmatter  →  pip install python-frontmatter")
    sys.exit(2)

try:
    import chromadb
    from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
except ImportError:
    print("ERRO: instale chromadb  →  pip install chromadb")
    sys.exit(2)

KB = Path(__file__).parent / "kb"
CHROMA_DIR = Path(__file__).parent / ".chroma"
COLLECTION = "projeto-kb"

SCORE_THRESHOLD = 0.25


def _make_ef(model_name: str | None = None):
    """Cria a embedding function. Sem model_name usa o default do ChromaDB (ONNX all-MiniLM-L6-v2)."""
    if model_name:
        from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

        return SentenceTransformerEmbeddingFunction(model_name=model_name)
    return DefaultEmbeddingFunction()


def _file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def _doc_id(path: Path, kb_root: Path) -> str:
    return str(path.relative_to(kb_root)).replace("\\", "/").replace(".md", "")


class SemanticIndex:
    def __init__(
        self,
        kb_root: Path = KB,
        chroma_dir: Path = CHROMA_DIR,
        model_name: str | None = None,
    ):
        self.kb_root = kb_root
        self.chroma_dir = chroma_dir
        self.ef = _make_ef(model_name)
        self.client = chromadb.PersistentClient(path=str(chroma_dir))
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION,
            embedding_function=self.ef,
            metadata={"hnsw:space": "cosine"},
        )

    def _parse(self, path: Path) -> dict:
        post = frontmatter.load(path)
        doc_id = _doc_id(path, self.kb_root)
        title = post.get("title", doc_id)
        description = post.get("description", "")
        tags = post.get("tags", [])
        text = f"{title}\n{description}\n{' '.join(map(str, tags))}\n{post.content}"
        return {
            "id": doc_id,
            "text": text,
            "metadata": {
                "title": title,
                "type": post.get("type", "Conceito"),
                "description": description,
                "tags": json.dumps(tags, ensure_ascii=False),
                "hash": _file_hash(path),
            },
        }

    def build(self) -> int:
        """Full reindex: apaga tudo e reindexa do zero."""
        try:
            self.client.delete_collection(COLLECTION)
        except ValueError:
            pass
        self.collection = self.client.create_collection(
            name=COLLECTION,
            embedding_function=self.ef,
            metadata={"hnsw:space": "cosine"},
        )

        docs = []
        for path in sorted(self.kb_root.glob("**/*.md")):
            try:
                docs.append(self._parse(path))
            except Exception:
                continue

        if docs:
            self.collection.add(
                ids=[d["id"] for d in docs],
                documents=[d["text"] for d in docs],
                metadatas=[d["metadata"] for d in docs],
            )
        return len(docs)

    def update(self) -> tuple[int, int, int]:
        """Incremental: indexa apenas novos/modificados e remove deletados.

        Returns (added, updated, removed).
        """
        existing: dict[str, str] = {}
        if self.collection.count() > 0:
            result = self.collection.get(include=["metadatas"])
            for id_, meta in zip(result["ids"], result["metadatas"]):
                existing[id_] = meta.get("hash", "")

        current_ids: set[str] = set()
        added = 0
        updated = 0

        for path in sorted(self.kb_root.glob("**/*.md")):
            try:
                doc = self._parse(path)
            except Exception:
                continue

            current_ids.add(doc["id"])
            old_hash = existing.get(doc["id"])

            if old_hash is None:
                self.collection.add(
                    ids=[doc["id"]],
                    documents=[doc["text"]],
                    metadatas=[doc["metadata"]],
                )
                added += 1
            elif old_hash != doc["metadata"]["hash"]:
                self.collection.update(
                    ids=[doc["id"]],
                    documents=[doc["text"]],
                    metadatas=[doc["metadata"]],
                )
                updated += 1

        stale = set(existing.keys()) - current_ids
        if stale:
            self.collection.delete(ids=list(stale))

        return added, updated, len(stale)

    def query(self, text: str, n_results: int = 5) -> list[dict]:
        """Busca semântica: retorna documentos mais similares com score."""
        if self.collection.count() == 0:
            return []

        n = min(n_results, self.collection.count())
        results = self.collection.query(
            query_texts=[text],
            n_results=n,
            include=["metadatas", "distances"],
        )

        hits = []
        for id_, meta, dist in zip(
            results["ids"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            score = round(1.0 - dist, 4)
            hits.append(
                {
                    "id": id_,
                    "type": meta.get("type", ""),
                    "title": meta.get("title", ""),
                    "description": meta.get("description", ""),
                    "score": score,
                }
            )
        return hits

    def count(self) -> int:
        return self.collection.count()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Indexa o bundle OKF para busca semântica.")
    parser.add_argument("--update", action="store_true", help="Incremental (apenas novos/modificados).")
    parser.add_argument("--kb", default=str(KB), help="Caminho raiz do bundle OKF.")
    parser.add_argument(
        "--model",
        default=None,
        help="Modelo sentence-transformers (omitir para usar default ONNX all-MiniLM-L6-v2).",
    )
    args = parser.parse_args()

    kb_root = Path(args.kb)
    if not kb_root.is_dir():
        print(f"ERRO: '{kb_root}' não é um diretório válido.")
        sys.exit(1)

    model_label = args.model or "default (all-MiniLM-L6-v2 via ONNX)"
    print(f"Modelo: {model_label}")
    print(f"Bundle: {kb_root}")
    idx = SemanticIndex(kb_root=kb_root, model_name=args.model)

    if args.update:
        added, updated, removed = idx.update()
        print(f"Incremental: {added} adicionados, {updated} atualizados, {removed} removidos.")
    else:
        total = idx.build()
        print(f"Reindex completo: {total} documentos indexados.")

    print(f"Total no índice: {idx.count()}")


if __name__ == "__main__":
    main()
