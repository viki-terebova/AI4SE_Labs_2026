import argparse
import json
import sys
from pathlib import Path

TASK_3_DIR = Path(__file__).resolve().parents[1] / "Task_3"
sys.path.insert(0, str(TASK_3_DIR))

from create_embeddings import embed_text

STORAGE_FILE = TASK_3_DIR / "embeddings.json"


def match_chunks(task: str, count: int = 5) -> list[dict]:
    task_embedding = embed_text(task)
    records = json.loads(STORAGE_FILE.read_text(encoding="utf-8"))
    matches = []
    for record in records:
        score = sum(
            left * right
            for left, right in zip(task_embedding, record["embedding"])
        )
        matches.append({
                "id": record["id"],
                "path": record["path"],
                "start_line": record["start_line"],
                "end_line": record["end_line"],
                "content": record["content"],
                "score": score,
            })
    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches[:count]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", help="Textual programming task")
    parser.add_argument("-n", "--count", type=int, default=5)
    args = parser.parse_args()
    print(json.dumps(match_chunks(args.task, args.count), indent=2))


if __name__ == "__main__":
    main()
