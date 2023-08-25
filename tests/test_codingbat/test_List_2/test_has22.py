from codingbat.List_2.has22 import has22


def test_has22() -> None:
    assert has22([1, 2, 2]) is True
    assert has22([1, 2, 1, 2]) is False
    assert has22([2, 1, 2]) is False
    assert has22([2, 2, 2, 1]) is True
