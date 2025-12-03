from pattern import find_pattern_multiple, find_pattern_multiple_regex, find_pattern_twice


def test_pattern_twice() -> None:
    assert find_pattern_twice("11-22") == {11, 22}
    assert find_pattern_twice("95-115") == {99}
    assert find_pattern_twice("998-1012") == {1010}
    assert find_pattern_twice("1188511880-1188511890") == {1188511885}
    assert find_pattern_twice("222220-222224") == {222222}
    assert find_pattern_twice("1698522-1698528") == set()
    assert find_pattern_twice("446443-446449") == {446446}
    assert find_pattern_twice("38593856-38593862") == {38593859}
    assert find_pattern_twice("565653-565659") == set()
    assert find_pattern_twice("824824821-824824827") == set()
    assert find_pattern_twice("2121212118-2121212124") == set()


def test_pattern_multiple() -> None:
    assert find_pattern_multiple("11-22") == {11, 22}
    assert find_pattern_multiple("95-115") == {99, 111}
    assert find_pattern_multiple("998-1012") == {999, 1010}
    assert find_pattern_multiple("1188511880-1188511890") == {1188511885}
    assert find_pattern_multiple("222220-222224") == {222222}
    assert find_pattern_multiple("1698522-1698528") == set()
    assert find_pattern_multiple("446443-446449") == {446446}
    assert find_pattern_multiple("38593856-38593862") == {38593859}
    assert find_pattern_multiple("565653-565659") == {565656}
    assert find_pattern_multiple("824824821-824824827") == {824824824}
    assert find_pattern_multiple("2121212118-2121212124") == {2121212121}


def test_pattern_multiple_alternative() -> None:
    assert find_pattern_multiple_regex("11-22") == {11, 22}
    assert find_pattern_multiple_regex("95-115") == {99, 111}
    assert find_pattern_multiple_regex("998-1012") == {999, 1010}
    assert find_pattern_multiple_regex("1188511880-1188511890") == {1188511885}
    assert find_pattern_multiple_regex("222220-222224") == {222222}
    assert find_pattern_multiple_regex("1698522-1698528") == set()
    assert find_pattern_multiple_regex("446443-446449") == {446446}
    assert find_pattern_multiple_regex("38593856-38593862") == {38593859}
    assert find_pattern_multiple_regex("565653-565659") == {565656}
    assert find_pattern_multiple_regex("824824821-824824827") == {824824824}
    assert find_pattern_multiple_regex("2121212118-2121212124") == {2121212121}
