#!/usr/bin/env python3
"""Write one original one-line roast of an everyday gadget to /output/entry.txt.

Standard library only. No network access, no input files.
"""

import os
import sys

ROAST = (
    "My robot vacuum has a 3D map of my whole flat and still eats the "
    "same charging cable every single day, like that is the job."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    line = ROAST.strip()

    if not line:
        print("error: roast line is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: roast line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: roast line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
