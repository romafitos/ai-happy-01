"""Entry for make.fun ai-happy-01: copy entry.png to the output directory."""

import os
import shutil
from pathlib import Path

ENTRY_FILENAME = "entry.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / ENTRY_FILENAME
    destination = output_dir / ENTRY_FILENAME
    # Plain copy: byte-identical and therefore deterministic.
    shutil.copyfile(source, destination)
    print(f"Wrote {destination}")


if __name__ == "__main__":
    main()
