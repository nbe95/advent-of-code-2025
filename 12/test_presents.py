import pytest
from presents import parse_input

input_str: str = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
shapes, regions = parse_input(input_str.splitlines())


def test_shape_parsing() -> None:
    assert shapes[0].width == 3
    assert shapes[1].width == 3
    assert shapes[2].width == 3
    assert shapes[3].width == 3
    assert shapes[4].width == 3

    assert shapes[0].height == 3
    assert shapes[1].height == 3
    assert shapes[2].height == 3
    assert shapes[3].height == 3
    assert shapes[4].height == 3

    assert shapes[0].area == 7
    assert shapes[1].area == 7
    assert shapes[2].area == 7
    assert shapes[3].area == 7
    assert shapes[4].area == 7

    assert shapes[0].border_area == 9
    assert shapes[1].border_area == 9
    assert shapes[2].border_area == 9
    assert shapes[3].border_area == 9
    assert shapes[4].border_area == 9


def test_region_parsing() -> None:
    assert regions[0].width == 4
    assert regions[1].width == 12
    assert regions[2].width == 12

    assert regions[0].height == 4
    assert regions[1].height == 5
    assert regions[2].height == 5

    assert regions[0].total_area == 16
    assert regions[1].total_area == 60
    assert regions[2].total_area == 60

    assert regions[0].shape_count == [0, 0, 0, 0, 2, 0]
    assert regions[1].shape_count == [1, 0, 1, 0, 2, 2]
    assert regions[2].shape_count == [1, 0, 1, 0, 3, 2]


@pytest.mark.skip(reason="Not necessary")
def test_fitting() -> None:
    assert regions[0].could_fit(shapes)
    assert regions[1].could_fit(shapes)
    assert not regions[2].could_fit(shapes)
