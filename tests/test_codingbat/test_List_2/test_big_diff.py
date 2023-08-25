from codingbat.List_2.big_diff import big_diff


def test_get_diff() -> None:
    assert big_diff([10, 4, 2, 3, 5]) == 8
    assert big_diff([2, 10, 7, 2]) == 8
