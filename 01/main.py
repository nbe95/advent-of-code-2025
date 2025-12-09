"""Advent of Code - 2025-12-01"""

import sys

from dial import Dial


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:
        lines = handle.readlines()
        dial = Dial()
        for command in lines:
            dial.rotate(command)

        print(f"Rotated the dial {len(lines)} times. Final position: {dial.get_pos()}.")
        print(f"Password: {dial.count(0)}.")
        print(f"Password with counting each tick: {dial.count(0, True)}.")

    return 0


if __name__ == "__main__":
    main()
