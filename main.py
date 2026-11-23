#!/usr/bin/env python3
"""Write one original one-line roast of an everyday gadget to /output/entry.txt.

Standard library only, no network access.
"""

import os
import sys

ROAST = (
    "My sleep tracker handed me a gold star for eight hours of sleep "
    "\u2014 all eight earned while I lay awake, watching it count."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = ROAST.strip()
    if not line:
        print("error: roast line is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: roast line must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 200:
        print(
            "error: roast line must be 1-200 characters, got %d" % len(line),
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
