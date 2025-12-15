"""Advent of Code - 2025-12-12"""

import sys

from presents import parse_input


def main() -> int:

    with open(sys.path[0] + "/input.txt", "r") as handle:

        shapes, regions = parse_input(handle.readlines())
        print(f"Parsed {len(regions)} regions and {len(shapes)} shapes.")

        fitting_regions: int = sum(region.could_fit(shapes) for region in regions)
        print(f"Found {fitting_regions} regions likely to fit the presents' shapes.")

    return 0


if __name__ == "__main__":
    main()
