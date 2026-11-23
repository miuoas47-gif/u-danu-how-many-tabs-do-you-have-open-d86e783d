#!/usr/bin/env python3
"""Write my honest open browser tab count to entry.txt.

The entry is a single number, digits only: 87 open browser tabs.
No words, no punctuation, no newline -- just the digits.
"""

import os
import sys

ENTRY = "87"


def validate(entry: str) -> bytes:
    """Return the entry as UTF-8 bytes, or raise if it breaks the gate."""
    if not entry:
        raise ValueError("entry is empty")
    if not entry.isascii() or not entry.isdigit():
        raise ValueError("entry must be digits only")
    if not 1 <= len(entry) <= 5:
        raise ValueError("entry must be 1 to 5 characters")
    if entry.strip() != entry:
        raise ValueError("entry must not contain whitespace")
    return entry.encode("utf-8")


def main() -> int:
    try:
        data = validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print(f"Wrote entry.txt: {ENTRY} ({len(data)} bytes, digits only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
