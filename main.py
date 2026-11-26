#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Office Artifacts: The One-Line Placard Contest".

Writes exactly one museum placard line (122 characters, a single line,
at most 180 characters, UTF-8) to /output/entry.txt. Deterministic: no
input, no randomness, no network.
"""

from pathlib import Path

ENTRY = (
    "Stapler, c. 1998. Jammed since the Clinton administration. Has stapled "
    "40,000 documents and exactly one tie; the tie sued."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
