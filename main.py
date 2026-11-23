#!/usr/bin/env python3
"""Write the office-joke entry to entry.txt in the configured output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
/output. The directory is created if missing. One UTF-8 file is written.
"""

import os
from pathlib import Path

ENTRY = (
    "I replied 'sounds good' to the wrong thread and approved my own PTO "
    "denial, and my boss thanked me for being decisive."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    (out_path / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
