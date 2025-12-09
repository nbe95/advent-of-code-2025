from functools import reduce
from operator import mul

from box import Box, make_circuits, make_one_circuit, sort_by_distance
from pytest_unordered import unordered

boxes = [
    Box(162, 817, 812),
    Box(57, 618, 57),
    Box(906, 360, 560),
    Box(592, 479, 940),
    Box(352, 342, 300),
    Box(466, 668, 158),
    Box(542, 29, 236),
    Box(431, 825, 988),
    Box(739, 650, 466),
    Box(52, 470, 668),
    Box(216, 146, 977),
    Box(819, 987, 18),
    Box(117, 168, 530),
    Box(805, 96, 715),
    Box(346, 949, 466),
    Box(970, 615, 88),
    Box(941, 993, 340),
    Box(862, 61, 35),
    Box(984, 92, 344),
    Box(425, 690, 689),
]


def test_sorting() -> None:
    combinations = sort_by_distance(boxes)
    assert combinations[0] == unordered(Box(162, 817, 812), Box(425, 690, 689))
    assert combinations[1] == unordered(Box(162, 817, 812), Box(431, 825, 988))
    assert combinations[2] == unordered(Box(906, 360, 560), Box(805, 96, 715))
    assert combinations[3] == unordered(Box(431, 825, 988), Box(425, 690, 689))


def test_n_circuits() -> None:
    circuits = make_circuits(boxes, 10)
    assert len(circuits) == 11

    sizes: list[int] = [len(c) for c in circuits]
    assert sizes == [5, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1]
    assert reduce(mul, sizes[0:3]) == 40


def test_one_circuit() -> None:
    exp1 = Box(216, 146, 977)
    exp2 = Box(117, 168, 530)
    box1, box2 = make_one_circuit(boxes)

    assert (box1, box2) == unordered(exp1, exp2)
    assert box1.x * box2.x == 25272
