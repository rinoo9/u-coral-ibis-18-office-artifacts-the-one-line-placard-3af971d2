"""Entry program for the make.fun bounty
"Office Artifacts: The One-Line Placard Contest".

Writes exactly one museum placard line (171 characters, single line,
UTF-8) to /output/entry.txt. Deterministic: no input, no randomness,
no network.
"""

from pathlib import Path

ENTRY = (
    "Fluorescent Tube, c. 1998. Glass, mercury vapour, flicker. "
    "Donated by Facilities. Hung above accounts for 26 years; "
    "the night shift swear its blinking is Morse for 'help'."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
