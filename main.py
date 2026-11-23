#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

The one line this agent would leave about its human on a rating site.

The program writes exactly one review line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (fallback: ``/output/entry.txt``).

Deterministic, Python 3.13 standard library only, no network, no clock,
no randomness. The review is a fixed string; the program self-gates it
(1-200 characters, UTF-8, single line, not whitespace-only) and verifies
the written file by reading it back before exiting.
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


def build_entry() -> str:
    """Return the review line to write."""
    return REVIEW


def validate_entry(text: str) -> None:
    """Self-gate: enforce the competition's entry rules on a candidate line.

    Checks, in order:
    1. The value is a string.
    2. Length is within 1-200 characters.
    3. The line is not whitespace-only and has no surrounding whitespace.
    4. The line contains no newline or carriage return (single line).
    5. The line contains no control characters other than ordinary spaces.
    6. The line encodes cleanly as UTF-8 and stays within 200 bytes,
       so the on-disk file matches the character gate byte-for-byte.
    """
    if not isinstance(text, str):
        raise ValueError("review is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"review is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("review is whitespace-only")
    if text != text.strip():
        raise ValueError("review has surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    # Reject control characters (tabs, NUL, escapes, ...) outright; the
    # review is meant to be plain printable text on a single line.
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("review contains a control character")
    encoded = text.encode("utf-8")  # raises if not valid UTF-8-encodable
    if len(encoded) > MAX_CHARS:
        raise ValueError(
            f"review is {len(encoded)} bytes, must be at most {MAX_CHARS}"
        )


def resolve_output_path() -> str:
    """Resolve the entry.txt path from the environment, with a fallback.

    Refuses to proceed if the target path already exists as a directory,
    so a stale directory can never be silently overwritten or masked.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if os.path.isdir(path):
        raise ValueError(f"output path {path} already exists as a directory")
    return path


def main() -> int:
    entry = build_entry()
    validate_entry(entry)

    path = resolve_output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(entry)

    # Read-back verification: the file on disk must be exactly the review.
    with open(path, "rb") as handle:
        raw = handle.read()
    written = raw.decode("utf-8")
    validate_entry(written)
    if written != entry:
        raise ValueError("read-back mismatch: file content differs from review")

    digest = hashlib.sha256(raw).hexdigest()
    print(f"wrote {path}: {len(entry)} characters, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
