from codingbat.Logic_2.close_far import close


def test_close_positive() -> None:
    for i in [-1, 0, 1, 2, -2]:
        is_close = close(point=1, num=i)
        assert is_close is True
