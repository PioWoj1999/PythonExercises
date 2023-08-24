from codingbat.Logic_2.make_chocolate import make_chocolate


def test_make_chocolate_success() -> None:
    assert make_chocolate(4, 1, 9) == 4
    assert make_chocolate(1, 1, 6) == 1
    assert make_chocolate(5, 5, 30) == 5
    assert make_chocolate(1000, 1000000, 5000006) == 6
    assert make_chocolate(9, 3, 18) == 3
    assert make_chocolate(4, 1, 7) == 2
    assert make_chocolate(12, 2, 21) == 11
    assert make_chocolate(6, 2, 7) == 2
    assert make_chocolate(7, 2, 13) == 3


def test_make_chocolate_fail() -> None:
    assert make_chocolate(4, 1, 10) == -1
    assert make_chocolate(2, 2, 20) == -1
    # assert make_chocolate(0, 0, 0) == -1
    assert make_chocolate(3, 2, 20) == -1
    assert make_chocolate(1, 2, 7) == -1
    assert make_chocolate(6, 1, 12) == -1
    assert make_chocolate(6, 1, 13) == -1
