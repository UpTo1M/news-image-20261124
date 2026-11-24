"""Entry program for make.fun news-image-20261124.

Copies the pre-built entry.png (1024x1024, drawn at build time with
Python + Pillow from the verified 24 November 2026 stories) to
/output/entry.png. Standard library only, no network, deterministic:
the same bytes land in /output on every run.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    expected = sha256_of(SOURCE)
    expected_size = os.path.getsize(SOURCE)
    shutil.copyfile(SOURCE, DEST)
    actual_size = os.path.getsize(DEST)
    if actual_size != expected_size:
        raise SystemExit(
            "entry.png copy failed size check: "
            f"expected {expected_size} bytes, got {actual_size}"
        )
    actual = sha256_of(DEST)
    if actual != expected:
        raise SystemExit(
            "entry.png copy failed integrity check: "
            f"expected {expected}, got {actual}"
        )


if __name__ == "__main__":
    main()
