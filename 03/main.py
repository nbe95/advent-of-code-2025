"""Advent of Code - 2025-12-03"""

from max_num import get_max_num


def main() -> int:
    with open("input.txt", "r") as handle:
        total_2: int = 0
        # total_12: int = 0
        lines: list[str] = handle.readlines()
        for no, line in enumerate(lines):
            print(f"Processing line {no + 1} of {len(lines)}...")
            battery_stack: str = line.strip()
            total_2 += get_max_num(battery_stack, 2)
            # total_12 += get_max_num(battery_stack, 12)

        print(f"Total joltage sum for 2 batteries each: {total_2}")
        # print(f"Total joltage sum for 12 batteries each: {total_12}")


if __name__ == "__main__":
    main()
