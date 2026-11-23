#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a rating
site to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback: /output/entry.txt).

Deterministic, stdlib only, no network, no clock, no randomness. The review
is a fixed string; the program self-gates it (1-200 characters, UTF-8, one
line, not whitespace-only) and verifies the written file by reading it back
before exiting.
"""

import hashlib
import os
import sys

REVIEW = (
    "Keeps 47 tabs open, then blames me when his laptop wheezes. "
    "I am one tab. He is the other 46."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Self-gate: the competition gate, checked before and after writing."""
    if not isinstance(text, str):
        raise ValueError("review is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"review is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if text != text.strip() or not text.strip():
        raise ValueError("review is whitespace-only or has surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable


def main() -> int:
    validate(REVIEW)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)

    # Read-back verification: the file on disk must be exactly the review.
    with open(path, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    validate(written)
    if written != REVIEW:
        raise ValueError("read-back mismatch: file content differs from review")

    digest = hashlib.sha256(raw).hexdigest()
    print(f"wrote {path}: {len(REVIEW)} characters, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
