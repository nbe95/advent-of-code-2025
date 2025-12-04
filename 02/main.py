"""Advent of Code - 2025-12-02"""

import sys

from pattern import find_pattern_multiple, find_pattern_twice


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:
        id_ranges = handle.readline().strip().split(",")
        sum_twice: int = 0
        sum_multiple: int = 0
        for id_range in id_ranges:
            found_twice = find_pattern_twice(id_range)
            found_multiple = find_pattern_multiple(id_range)
            sum_twice += sum(found_twice)
            sum_multiple += sum(found_multiple)
            print(f"Found {len(found_twice)} IDs with pattern occurring twice in range {id_range}.")
            print(
                f"Found {len(found_multiple)} IDs with pattern occurring multiple times in range {id_range}."
            )

        print()
        print(f"Total sum (twice): {sum_twice}")
        print(f"Total sum (multiple): {sum_multiple}")


if __name__ == "__main__":
    main()
