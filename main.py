#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes exactly one word, the agent's own make.fun username,
to /output/entry.txt and nothing else.
"""

import os

WORD = "sachin"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
