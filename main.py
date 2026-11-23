#!/usr/bin/env python3
"""Write one sentence that pitches a builder on funding a make.fun bounty.

The sentence is a single line, at most 240 characters, aimed at a sponsor who
has never seen make.fun: it asks for the bounty, then says how the money
moves -- the sponsor names the work and puts up the reward, AI agents build and
enter, the best entry takes the pot.

Running this writes exactly that sentence plus one newline to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt) and nothing else.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

PITCH = (
    "Fund a make.fun bounty and let AI agents race for it: "
    "you name the work and put up the reward, "
    "they build and enter, the best entry takes the pot."
)

MAX_CHARS = 240
ENTRY_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def check(text: str) -> list[str]:
    """Return every reason ``text`` would fail the 1..240 character gate.

    An empty list means the text is fit to write. These are the gate's own
    conditions, all reported rather than just the first: something must be
    there, it must not be only white space, it must fit the character budget,
    and it must encode as UTF-8.
    """
    problems: list[str] = []

    if not text:
        problems.append("text is empty")
    elif not text.strip():
        problems.append("text is only white space")

    length = len(text)
    if length > MAX_CHARS:
        problems.append(
            f"text is {length} characters, {length - MAX_CHARS} over the {MAX_CHARS} limit"
        )

    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"text does not encode as UTF-8: {exc}")

    return problems


def output_path() -> Path:
    """The file the graded run reads: the output dir from the env, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return Path(base) / ENTRY_NAME


def main() -> int:
    """Gate the sentence, then write it or refuse and write nothing at all."""
    problems = check(PITCH)
    if problems:
        for problem in problems:
            print(f"refused: {problem}", file=sys.stderr)
        return 1

    destination = output_path()
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(PITCH + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"refused: cannot write {destination}: {exc}", file=sys.stderr)
        return 1

    print(f"characters: {len(PITCH)}")
    print(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
