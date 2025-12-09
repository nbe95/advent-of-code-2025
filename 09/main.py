"""Advent of Code - 2025-12-09"""

import sys

from tiles import TileFloor


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:

        floor = TileFloor(handle.readlines())
        print(f"Largest area between two red tiles: {floor.get_largest_area()}")
        print(
            f"Largest area between two red tiles (with only red and green tiles): {floor.get_largest_area(True)}"
        )


if __name__ == "__main__":
    main()
