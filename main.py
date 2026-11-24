#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why A: coffee is the more vivid answer. It is the drink with a jolt —
bitter, dark, urgent, the one that drags a morning into being — while tea
waits politely. And "A" is the top grade: coffee is the A-grade answer in
the coffee-against-tea argument. One letter, nothing else.
"""

import os

LETTER = "A"  # A for coffee


def main() -> None:
    # Guard the gate: exactly one letter, A for coffee or B for tea.
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        raise ValueError("entry must be exactly one letter, A or B")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
