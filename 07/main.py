"""Advent of Code - 2025-12-07"""

import sys

from manifold import TachyonManifold


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:

        m = TachyonManifold([line.strip() for line in handle.readlines()])
        m.process_beam()
        print(f"Total times the Tachyon Manifold beam was split: {m.count_splits()}")
        print(f"Possible number of distinct timelines: {m.count_paths()}")


if __name__ == "__main__":
    main()
