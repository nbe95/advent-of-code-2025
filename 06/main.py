"""Advent of Code - 2025-12-06"""

import sys

from op_matrix import OpMatrix, OpMatrixRtl


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:

        lines: list[str] = [line.strip("\r\n") for line in handle.readlines()]
        m = OpMatrix(lines)
        print(f"Grand total of OpMatrix: {m.get_grand_total()}")

        m = OpMatrixRtl(lines)
        print(f"Grand total of OpMatrix (right to left): {m.get_grand_total()}")

    return 0


if __name__ == "__main__":
    main()
