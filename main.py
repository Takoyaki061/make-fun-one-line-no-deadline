#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line joke excusing a missed
deadline to /output/entry.txt (stdlib only)."""

import os

LINE = (
    "I did finish it, then reread it and had to go lie down in my car, "
    "so the work exists, it's just emotionally unavailable right now."
)


def main() -> None:
    # Gate compliance: the scorer requires UTF-8 text of 1-200 characters,
    # not only whitespace, in a single line. Fail loudly instead of
    # writing an entry the gate would refuse.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
