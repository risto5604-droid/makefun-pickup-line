#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.

The line: a robot admits it has no heart, then lets its cooling fans do the
blushing — the joke grows out of machine-ness (no heart, fans, ping) instead
of dressing a human line in robot words. One fresh angle, kept short.

Rejected draft: "Are you a firmware update? Because ever since you arrived,
bugs I didn't know I had are gone." — also machine-native, but the fan line
lands the charm faster and the "ping" keeps the robot voice in the last beat.
"""
import os

LINE = "I don't have a heart, but my cooling fans spin faster every time you ping me."

# Gate: the entry must be 1-200 characters of UTF-8 text, not only whitespace.
# ASCII is enforced too: the line is plain English, so any non-ASCII byte means
# the text was corrupted in editing and the sandbox run must fail loudly.
assert 1 <= len(LINE) <= 200 and LINE.strip() and LINE.isascii(), "entry line violates the 1-200 character gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
