import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

ASSIGNMENTS_DIR = Path(__file__).resolve().parents[1]
PLAYGROUND_ROOT = ASSIGNMENTS_DIR / "playground"
MANIFEST_FILE = ASSIGNMENTS_DIR / "missing_code.json"
TASK_4_DIR = ASSIGNMENTS_DIR / "Task_4"
MODEL = "gpt-6-luna"

load_dotenv(ASSIGNMENTS_DIR / ".env")

sys.path.insert(0, str(TASK_4_DIR))
from match_embeddings import match_chunks

def build_prompt(task: str, target_path: str, matches: list[dict]) -> str:
    target_file = PLAYGROUND_ROOT / target_path
    context = "\n\n".join(
        f"FILE: {match['path']} LINES {match['start_line']}-{match['end_line']}\n"
        f"{match['content']}"
        for match in matches
    )

    return f"""Implement exactly the requested method in the target Python file.
Preserve all other code and behavior. Return the complete resulting target file.
Do not use Markdown fences or explanations.

TASK:
{task}

TARGET FILE: {target_path}
CURRENT TARGET FILE:
{target_file.read_text(encoding='utf-8')}

RETRIEVED REPOSITORY CONTEXT:
{context}
"""


def call_llm(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing")

    client = OpenAI(
        api_key=api_key,
        base_url=os.getenv("OPENAI_BASE_URL") or None,
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    source_code = response.choices[0].message.content
    if not source_code:
        raise RuntimeError("The model returned no source code")

    source_code = source_code.strip()
    if source_code.startswith("```"):
        lines = source_code.splitlines()[1:]
        if lines and lines[-1].strip() == "```":
            lines.pop()
        source_code = "\n".join(lines)
    return source_code + "\n"


def solve_task(task: str, target_path: str) -> None:
    matches = match_chunks(task, count=5)
    prompt = build_prompt(task, target_path, matches)
    source_code = call_llm(prompt)
    (PLAYGROUND_ROOT / target_path).write_text(source_code, encoding="utf-8")


def main() -> None:
    specifications = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    for index, specification in enumerate(specifications, start=1):
        task = (
            f"In {specification['file']}, implement "
            f"{specification['class']}.{specification['method']}. "
            f"Required behavior: {specification['docstring'].strip()}"
        )
        print(f"[{index}/{len(specifications)}] {specification['class']}.{specification['method']}")
        solve_task(task, specification["file"])


if __name__ == "__main__":
    main()
