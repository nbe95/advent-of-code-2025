from max_num import get_max_num


def test_max_num() -> None:
    assert get_max_num("987654321111111", 2) == 98
    assert get_max_num("811111111111119", 2) == 89
    assert get_max_num("234234234234278", 2) == 78
    assert get_max_num("818181911112111", 2) == 92

    assert get_max_num("987654321111111", 12) == 987654321111
    assert get_max_num("811111111111119", 12) == 811111111119
    assert get_max_num("234234234234278", 12) == 434234234278
    assert get_max_num("818181911112111", 12) == 888911112111
