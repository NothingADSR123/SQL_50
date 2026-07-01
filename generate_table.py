from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
README_PATH = ROOT / "README.md"

FOLDER_MAP = [
    {
        "key": "leetcode_sql",
        "title": "LeetCode SQL Practice",
        "folder": ROOT / "solutions",
        "numbered": True,
    },
]

# Regex looking for standard LeetCode numbering format ending with .sql
NUMBERED_FILE_RE = re.compile(r"^(?P<number>\d+)\.(?P<name>.+)\.sql$", re.IGNORECASE)


def escape_table_text(value: str) -> str:
    return value.replace("|", r"\|")


def relative_link(path: Path) -> str:
    return quote(path.relative_to(ROOT).as_posix(), safe="/")


def display_name(file_path: Path, numbered: bool) -> tuple[int, str]:
    stem = file_path.stem
    if numbered:
        match = NUMBERED_FILE_RE.match(file_path.name)
        if not match:
            return (10**12, stem)
        return (int(match.group("number")), match.group("name"))
    return (0, stem)


def collect_files(folder: Path, numbered: bool) -> list[Path]:
    if not folder.exists():
        return []
    
    # Collect all .sql files instead of .py
    files = [path for path in folder.iterdir() if path.is_file() and path.suffix.lower() == ".sql"]
    
    if numbered:
        files = [path for path in files if NUMBERED_FILE_RE.match(path.name)]
        files.sort(key=lambda path: display_name(path, True))
    else:
        files.sort(key=lambda path: path.stem.lower())
    return files


def render_table(files: Iterable[Path], numbered: bool) -> str:
    rows = ["| # | Problem | Link |", "|---|---------|------|"]
    files = list(files)
    if not files:
        rows.append("| - | No solution files found | - |")
        return "\n".join(rows)

    for index, file_path in enumerate(files, start=1):
        _, problem = display_name(file_path, numbered)
        rows.append(
            f"| {index} | {escape_table_text(problem)} | [Code]({relative_link(file_path)}) |"
        )
    return "\n".join(rows)


def render_section(config: dict[str, object]) -> str:
    folder = config["folder"]
    assert isinstance(folder, Path)
    numbered = bool(config["numbered"])
    title = str(config["title"])
    key = str(config["key"])
    files = collect_files(folder, numbered)
    table = render_table(files, numbered)
    summary = f"<summary>{escape_table_text(title)} ({len(files)})</summary>"
    marker_start = f""
    marker_end = f""
    return "\n".join(
        [
            marker_start,
            summary,
            "",
            table,
            marker_end,
        ]
    )


def replace_section(readme: str, key: str, section: str) -> str:
    start_marker = f""
    end_marker = f""
    pattern = re.compile(
        rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        re.DOTALL,
    )
    if not pattern.search(readme):
        raise ValueError(f"Missing markers for {key}")
    return pattern.sub(section, readme, count=1)


def main() -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    updated = readme
    for config in FOLDER_MAP:
        updated = replace_section(updated, str(config["key"]), render_section(config))

    if updated != readme:
        README_PATH.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()