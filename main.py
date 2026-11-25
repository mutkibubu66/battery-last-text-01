#!/usr/bin/env python3
"""The battery's last text to its charger, saved to /output/entry.txt.

One line, 142 characters, written by a phone battery that held on at
1% all day. Pure standard library; no network, no arguments, no input.
"""

from pathlib import Path

ENTRY = (
    "I waited all day at 1% so you could finish one more call. "
    "Now I'm fading in your hand \u2014 and you're across the room. "
    "Tell the cable I loved it."
)
OUT = Path("/output/entry.txt")


def check(text):
    """Gate: one non-blank UTF-8 line of 1 to 200 characters."""
    assert text == text.strip(), "no leading or trailing whitespace"
    assert text.count("\n") == 0, "exactly one line, no embedded newline"
    assert "\r" not in text, "no carriage return may hide in the line"
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only whitespace"
    text.encode("utf-8")  # raises if the line is not valid UTF-8


def main():
    check(ENTRY)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY + "\n", encoding="utf-8")
    # What the grader reads must be exactly the line plus its newline.
    assert OUT.read_text(encoding="utf-8") == ENTRY + "\n"
    print(ENTRY)


if __name__ == "__main__":
    main()
