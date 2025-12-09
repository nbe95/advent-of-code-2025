from dataclasses import dataclass


@dataclass
class Box:
    x: int
    y: int
    z: int

    @classmethod
    def from_string(cls, string: str) -> "Box":
        x, y, z = string.split(",")
        return cls(int(x), int(y), int(z))

    def calc_sq_distance(self, other: "Box") -> float:
        # Squared distance is sufficient for comparison/ordering
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2


def sort_by_distance(boxes: list[Box]) -> list[tuple[Box, Box]]:
    """Compare each box against each other and sort results by Euclidean distance"""
    combinations: list[tuple[Box, Box]] = []
    for index in range(len(boxes)):
        combinations.extend((boxes[index], boxes[cmp]) for cmp in range(index + 1, len(boxes)))
    return sorted(combinations, key=lambda c: c[0].calc_sq_distance(c[1]))


def _merge_circuits(circuits: list[list[Box]], box1: Box, box2: Box) -> list[list[Box]]:
    """Merge two circuits including box1 and box2"""
    merged: list[Box] = []
    non_affected: list[list[Box]] = []

    for circuit in circuits:
        # Remove any existing circuits with the next to boxes to merge
        if box1 in circuit or box2 in circuit:
            merged.extend(circuit)
        else:
            non_affected.append(circuit)
    return non_affected + [merged]


def make_circuits(boxes: list[Box], num_to_connect: int) -> list[list[Box]]:
    """Make groups of circuits (descending in size) by connecting the closest n boxes"""

    # Start with each box in an individual circuit
    circuits: list[list[Box]] = [[box] for box in boxes]
    boxes_by_dist: list[tuple[Box, Box]] = sort_by_distance(boxes)

    for _ in range(num_to_connect):
        box1, box2 = boxes_by_dist.pop(0)
        circuits = _merge_circuits(circuits, box1, box2)

    return sorted(circuits, key=len, reverse=True)


def make_one_circuit(boxes: list[Box]) -> tuple[Box, Box]:
    """Make one single circuit and return the last two boxes which need to be connected"""

    # Start with each box in an individual circuit
    circuits: list[list[Box]] = [[box] for box in boxes]
    boxes_by_dist: list[tuple[Box, Box]] = sort_by_distance(boxes)

    while len(circuits) > 1:
        box1, box2 = boxes_by_dist.pop(0)
        circuits = _merge_circuits(circuits, box1, box2)

    return box1, box2
