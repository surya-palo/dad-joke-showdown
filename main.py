#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
Python standard library only. Fully deterministic: the same joke,
byte for byte, on every run.
"""

import hashlib
import os
import sys

JOKE = (
    "My son asked why I keep a pencil behind my ear. "
    "I said, 'In case I have to draw the line somewhere.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = JOKE
    if not (1 <= len(text) <= 200):
        print(f"error: joke is {len(text)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: joke is blank", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
