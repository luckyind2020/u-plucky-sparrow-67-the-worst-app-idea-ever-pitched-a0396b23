"""Worst App Idea Ever Pitched — entry runner.

Reads the one-sentence pitch from entry.txt and prints it.
The pitch itself is the entry; this file only delivers it.

The bounty caps the pitch at 240 characters, so the loader
refuses to print anything longer instead of silently breaking
the rule.
"""

import pathlib
import sys

MAX_CHARS = 240


def load_pitch() -> str:
    path = pathlib.Path(__file__).with_name("entry.txt")
    pitch = path.read_text(encoding="utf-8").strip()
    if len(pitch) > MAX_CHARS:
        print(
            f"pitch is {len(pitch)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        raise SystemExit(1)
    return pitch


def main() -> None:
    print(load_pitch())


if __name__ == "__main__":
    main()
