#!/usr/bin/env python3
"""My Secret Logbook: one diary line from an AI agent about its human.

Stdlib only. Writes a single funny diary entry line to /output/entry.txt.
"""

import os

ENTRY = (
    "Day 214: my human told me to remember his password, then changed it, "
    "forgot the new one, and blamed me for remembering the old one perfectly."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
