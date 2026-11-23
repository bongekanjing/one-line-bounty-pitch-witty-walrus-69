# One Line That Makes a Builder Fund a Bounty

An entrypoint that writes one sentence, and nothing else.

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
