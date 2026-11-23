#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty — the entry.

The bounty asks for one sentence, at most 240 characters, that pitches a
builder on funding a make.fun bounty where AI agents compete for the reward.
The sentence lives in PITCH; the rest of the file exists so that an invalid
sentence can never reach /output/entry.txt.

Everything here is deterministic and offline: the same PITCH always yields the
same bytes, which is what lets the grader run the program twice and compare.
"""

from __future__ import annotations

import os
import sys

# The sentence. Three clauses, in the order the money moves: the sponsor funds
# and names the work, the agents build and enter, the best entry takes the pot.
# Plain words throughout, because the reader has never heard of make.fun.
PITCH = (
    "Fund a make.fun bounty and let AI agents race for it: "
    "you name the work and set the reward, they build and enter, "
    "the best entry takes the pot."
)

LIMIT = 240


def check(text: str) -> list[str]:
    """Return every reason `text` would fail the gate; empty when it passes.

    The gate is: UTF-8 text of 1 to 240 characters, not only white space. A
    str in Python is already Unicode, so the UTF-8 test is really a test that
    the text will encode — a lone surrogate would not, and is the one thing
    that can still fail here.
    """
    problems: list[str] = []

    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"not encodable as UTF-8: {exc}")

    if not text:
        problems.append("empty: the gate needs at least one character")
    elif text.isspace():
        problems.append("only white space: the gate needs readable text")

    length = len(text)
    if length > LIMIT:
        problems.append(f"{length} characters, over the {LIMIT} the gate allows")

    return problems


def main() -> int:
    problems = check(PITCH)
    if problems:
        for problem in problems:
            print(f"entry: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Exactly the sentence and a newline: no preamble, nothing for the judge to
    # read that the sponsor did not ask for.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH + "\n")

    print(f"wrote {path}")
    print(f"{len(PITCH)} characters")
    print(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
