from grid import PaperGrid


def test_paper_grid() -> None:
    grid = PaperGrid(
        [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
    )
    assert grid.remove_accessible_rolls() == 13
    assert grid.remove_accessible_rolls() == 12
    assert grid.remove_accessible_rolls() == 7
    assert grid.remove_accessible_rolls() == 5
    assert grid.remove_accessible_rolls() == 2
    assert grid.remove_accessible_rolls() == 1
    assert grid.remove_accessible_rolls() == 1
    assert grid.remove_accessible_rolls() == 1
    assert grid.remove_accessible_rolls() == 1
    assert grid.remove_accessible_rolls() == 0
