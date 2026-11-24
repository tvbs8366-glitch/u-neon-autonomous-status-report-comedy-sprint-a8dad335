#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one original funny status-report line from an AI agent to its human
to /output/entry.txt. Deterministic by design: no input files, no network, no
randomness, stdlib only.
"""

import os
import sys

LINE = "Blockers: none. Risks: one \u2014 you keep saying 'just one small change' and I keep believing you."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> str | None:
    """Return an error message if the line breaks the rules, else None.

    Validate: one non-blank line, 1-200 characters.
    """
    if not line or not line.strip():
        return "line must not be blank"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if not 1 <= len(line) <= 200:
        return "line must be 1-200 characters, got %d" % len(line)
    return None


def main() -> int:
    error = validate_line(LINE)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read back and verify the file holds exactly what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE + "\n":
        print("error: written file does not match the status line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
