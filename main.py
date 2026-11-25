"""Worst AI Advice - a make.fun one-liner entry.

Writes a single line of catastrophically confident AI advice to
entry.txt in the output directory (MAKEFUN_OUTPUT_DIR, or /output
when the variable is not set). The advice is delivered in the tidy,
helpful voice of a real AI assistant, which is exactly what makes
it dangerous: it sounds plausible, it is specific enough to follow,
and anyone who follows it will regret it immediately.
"""

import os
from pathlib import Path

MAX_CHARS = 140  # the competition gate accepts 1..140 characters

LINE = (
    "For a cleaner, happier inbox, reply to every spam email — senders "
    "remove you faster once they know the address is active and friendly."
)


def check_line(line: str) -> str:
    """Refuse to write a line the gate would reject: blank or over-long."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars; the gate allows at most {MAX_CHARS}"
        )
    return line


def output_path() -> Path:
    """Resolve where entry.txt goes: $MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def main() -> None:
    text = check_line(LINE)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
