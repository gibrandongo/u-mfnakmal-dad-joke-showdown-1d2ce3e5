#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3.13 stdlib only. Deterministic: no clock,
no network, no randomness.
"""

import os

JOKE = (
    "I keep all my dad jokes in a spreadsheet. "
    "My wife calls it a database \u2014 I call it a dad-a-base."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate guard: the sealed scorer requires 1-200 characters,
    # not whitespace-only, as UTF-8 text.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be whitespace-only"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    JOKE.encode("utf-8")  # raises if the text is not valid UTF-8
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
