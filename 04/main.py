"""Advent of Code - 2025-12-04"""

import sys

from grid import PaperGrid


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:
        grid = PaperGrid([line.strip() for line in handle.readlines()])

        iteration: int = 0
        accessible: int = -1
        total_removed: int = 0
        while accessible != 0:
            iteration += 1
            accessible = grid.remove_accessible_rolls()
            total_removed += accessible
            print(f"Iteration {iteration:3} - Accessible paper rolls: {accessible}")

        print(f"Total removed paper rolls: {total_removed}")

    return 0


if __name__ == "__main__":
    main()
