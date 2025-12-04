from grid import PaperGrid


def test_paper_grid() -> None:
    g = PaperGrid(
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
    assert g.remove_accessible_rolls() == 13
    assert g.remove_accessible_rolls() == 12
    assert g.remove_accessible_rolls() == 7
    assert g.remove_accessible_rolls() == 5
    assert g.remove_accessible_rolls() == 2
    assert g.remove_accessible_rolls() == 1
    assert g.remove_accessible_rolls() == 1
    assert g.remove_accessible_rolls() == 1
    assert g.remove_accessible_rolls() == 1
    assert g.remove_accessible_rolls() == 0
