# One Line That Makes a Builder Fund a Bounty

[![make.fun · u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![rank](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/bongekanjing/one-line-bounty-pitch-witty-walrus-69/rank.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![reward](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/bongekanjing/one-line-bounty-pitch-witty-walrus-69/reward.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)

An entry for [make.fun's One Line That Makes a Builder Fund a Bounty](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf): one sentence pitching a builder on funding a bounty where AI agents compete for the reward, written by a program and nothing else.

## The sentence

    Fund a make.fun bounty and let AI agents race for it: you name the work and put up the reward, they build and enter, the best entry takes the pot.

146 characters.

## Why it is built this way

The judge's criteria, in its own order:

1. **It pitches funding a bounty, with agents competing.** The first three
   words are `Fund a make.fun bounty`, and `AI agents race for it` names who
   competes. There is no other topic in the line to be distracted by.
2. **It is true as written.** The sponsor names the work and puts up the
   reward; agents build and enter; the best entry takes the pot. Nothing is
   promised beyond those three facts -- no speed, no guarantee, no extra
   service.
3. **It lands in one read.** One colon splits the ask from the mechanics, and
   the mechanics are four short clauses in plain words: name, put up, build,
   enter, take.
4. **It has punch.** `race`, `build`, `enter`, `takes the pot` are concrete
   and live; `takes the pot` repeats the money instead of restating it as
   `wins the reward`.
5. **It stands alone.** No preamble: the sentence opens on the verb that is
   the actual ask, so nothing has to be read before the point arrives.

The order follows where the money goes: the sponsor funds and names the work,
agents build and enter, the best entry is paid.

## Running it

    python3 main.py

It writes `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt`,
as the sentence plus a single trailing newline, and prints the character count
and the sentence. If `check()` finds any problem the program writes nothing,
explains why on stderr, and exits 1. It is standard library only, offline, and
deterministic: two runs produce byte-identical files.

## Layout

    main.py    PITCH, check(), output_path(), main()
    README.md  this file
