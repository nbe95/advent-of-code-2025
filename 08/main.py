"""Advent of Code - 2025-12-08"""

import sys
from functools import reduce
from operator import mul

from box import Box, make_circuits, make_one_circuit


def main() -> int:
    with open(sys.path[0] + "/input.txt", "r") as handle:

        boxes = [Box.from_string(line.strip()) for line in handle.readlines()]
        print(f"Total number of junction boxes: {len(boxes)}")

        circuits = make_circuits(boxes, 1000)
        print(
            f"Number of circuits after connecting the closest 1000 junction boxes: {len(circuits)}"
        )

        result = reduce(mul, (len(c) for c in circuits[0:3]))
        print(f"Product of the three largest circuits' sizes: {result}")

        last_boxes = make_one_circuit(boxes)
        product: int = reduce(mul, (box.x for box in last_boxes))
        print(
            f"Product of x coordinates of the last 2 boxes needed to form one single circuit: "
            f"{product}"
        )

    return 0


if __name__ == "__main__":
    main()
