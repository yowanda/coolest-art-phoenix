#!/usr/bin/env python3
"""Entry program for make.fun coolest-art-01.

Writes the phoenix artwork (entry.png, stored next to this script) to
/output/entry.png. Pure stdlib, no network, fully deterministic: the output
is a byte-for-byte copy of the stored image, so every run produces the
exact same file.
"""

import pathlib

SOURCE_NAME = "entry.png"
OUTPUT_DIR = pathlib.Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.png"


def main() -> None:
    here = pathlib.Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = source.read_bytes()
    OUTPUT_PATH.write_bytes(data)


if __name__ == "__main__":
    main()

# Deterministic by design: copying fixed bytes means both sealed runs match.
