#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Coins one new English word and defines it in a single clear line, then
writes that line to /output/entry.txt for the house judge.

Pure standard library, deterministic: the same bytes on every run.
"""

import os

WORD = "sockwidow"
DEFINITION = "the lone sock left after its partner vanishes in the wash."
ENTRY = WORD + " \u2014 " + DEFINITION


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= 140:
        raise SystemExit("entry is %d characters, must be 1-140" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
