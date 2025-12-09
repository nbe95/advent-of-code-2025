"""Advent of Code - 2025-12-03"""

import sys

from max_num import get_max_num


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:
        total_2: int = 0
        total_12: int = 0
        lines: list[str] = handle.readlines()
        for _, line in enumerate(lines):
            battery_stack: str = line.strip()
            total_2 += get_max_num(battery_stack, 2)
            total_12 += get_max_num(battery_stack, 12)

        print(f"Total joltage sum for 2 batteries each: {total_2}")
        print(f"Total joltage sum for 12 batteries each: {total_12}")

    return 0


if __name__ == "__main__":
    main()
