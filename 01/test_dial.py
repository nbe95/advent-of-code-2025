import pytest
from dial import Dial


def test_overflow() -> None:
    d = Dial(0)
    assert d.get_pos() == 0

    d.rotate("L0")
    assert d.get_pos() == 0

    d.rotate("L5")
    assert d.get_pos() == 95

    d.rotate("R12")
    assert d.get_pos() == 7

    d.rotate("R1000")
    assert d.get_pos() == 7


def test_count() -> None:
    d = Dial(0)
    d.rotate("R1")
    d.rotate("R1")
    d.rotate("L1")

    assert d.count(0) == 0
    assert d.count(1) == 2
    assert d.count(2) == 1


def test_error_handling() -> None:
    d = Dial()
    d.rotate("r1")

    with pytest.raises(ValueError):
        d.rotate("foo")


def test_example() -> None:
    d = Dial()

    d.rotate("L68")
    assert d.get_pos() == 82

    d.rotate("L30")
    assert d.get_pos() == 52

    d.rotate("R48")
    assert d.get_pos() == 0

    d.rotate("L5")
    assert d.get_pos() == 95

    d.rotate("R60")
    assert d.get_pos() == 55

    d.rotate("L55")
    assert d.get_pos() == 0

    d.rotate("L1")
    assert d.get_pos() == 99

    d.rotate("L99")
    assert d.get_pos() == 0

    d.rotate("R14")
    assert d.get_pos() == 14

    d.rotate("L82")
    assert d.get_pos() == 32

    assert d.count(0) == 3
    assert d.count(0, True) == 6
