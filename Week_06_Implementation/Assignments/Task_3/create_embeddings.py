import hashlib
import json
import math
import re
from pathlib import Path

EMBEDDING_SIZE = 1024
CHUNKS_FILE = Path(__file__).resolve().parents[1] / "Task_2" / "chunks.json"
OUTPUT_FILE = Path(__file__).resolve().parent / "embeddings.json"
TOKEN_PATTERN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+")


def embed_text(text: str) -> list[float]:
    vector = [0.0] * EMBEDDING_SIZE
    for token in TOKEN_PATTERN.findall(text.lower()):
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        index = int.from_bytes(digest[:4], "big") % EMBEDDING_SIZE
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[index] += sign
    length = math.sqrt(sum(value * value for value in vector))
    if length:
        vector = [value / length for value in vector]
    return vector

def main() -> None:
    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    records = []
    for chunk in chunks:
        text = f"{chunk['path']}\n{chunk['content']}"
        records.append({**chunk, "embedding": embed_text(text)})
    OUTPUT_FILE.write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Saved {len(records)} embeddings to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
