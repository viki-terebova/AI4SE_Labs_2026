import json
from pathlib import Path

CHUNK_SIZE = 100
OVERLAP = 10
REPOSITORY_ROOT = Path(__file__).resolve().parents[1] / "playground"
OUTPUT_FILE = Path(__file__).resolve().parent / "chunks.json"


def create_chunks(repository_root: Path) -> list[dict]:
    chunks = []
    for file_path in sorted(repository_root.rglob("*.py")):
        if "tests" in file_path.relative_to(repository_root).parts:
            continue
        lines = file_path.read_text(encoding="utf-8").splitlines()
        start = 0
        while start < len(lines):
            end = min(start + CHUNK_SIZE, len(lines))
            relative_path = file_path.relative_to(repository_root).as_posix()
            chunks.append(
                {
                    "id": f"{relative_path}:{start + 1}-{end}",
                    "path": relative_path,
                    "start_line": start + 1,
                    "end_line": end,
                    "content": "\n".join(lines[start:end]),
                }
            )
            if end == len(lines):
                break
            start = end - OVERLAP
    return chunks

def main() -> None:
    chunks = create_chunks(REPOSITORY_ROOT)
    OUTPUT_FILE.write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Saved {len(chunks)} chunks to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
