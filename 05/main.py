"""Advent of Code - 2025-12-05"""

import sys

from ingredients import IngredientDb


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:
        db = IngredientDb([line.strip() for line in handle.readlines()])

        available_and_fresh: set[int] = db.get_fresh_and_available()
        print(f"Number of available and fresh ingredients: {len(available_and_fresh)}")

        num_fresh: int = db.count_fresh()
        print(f"Total number of fresh ingredients: {num_fresh}")


if __name__ == "__main__":
    main()
