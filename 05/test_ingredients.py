from ingredients import IngredientDb


def test_ingredients() -> None:
    db = IngredientDb(["3-5", "10-14", "16-20", "12-18", "", "1", "5", "8", "11", "17", "32"])
    assert db.get_fresh_and_available() == {5, 11, 17}
    assert db.count_fresh() == 14


def test_range_merging() -> None:
    assert IngredientDb._merge_ranges([]) == []
    assert IngredientDb._merge_ranges([(1, 2)]) == [(1, 2)]
    assert IngredientDb._merge_ranges([(1, 5), (1, 5)]) == [(1, 5)]
    assert IngredientDb._merge_ranges([(1, 4), (4, 5)]) == [(1, 5)]
    assert IngredientDb._merge_ranges([(1, 10), (2, 3), (4, 5)]) == [(1, 10)]
    assert IngredientDb._merge_ranges([(1, 5), (3, 7), (10, 12), (6, 8), (1, 2), (15, 18)]) == [
        (1, 8),
        (10, 12),
        (15, 18),
    ]
    assert IngredientDb._merge_ranges([(1, 3), (2, 6), (8, 10), (15, 18)]) == [
        (1, 6),
        (8, 10),
        (15, 18),
    ]
