from manifold import TachyonManifold

manifold = TachyonManifold(
    [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]
)
manifold.process_beam()


def test_splitting() -> None:
    assert manifold.count_splits() == 21


def test_timelines() -> None:
    assert manifold.count_paths() == 40
