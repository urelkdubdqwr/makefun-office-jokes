#!/usr/bin/env python3
"""Write the office-joke entry to entry.txt in the configured output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
/output. The directory is created if missing, and the entry is written as a
single UTF-8 file with one trailing newline.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "I replied 'sounds good' to the wrong thread and approved my own PTO "
    "denial, and my boss thanked me for being decisive."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(output_dir)
    try:
        out_path.mkdir(parents=True, exist_ok=True)
        (out_path / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot write entry to {out_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
