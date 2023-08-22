from close_far_6 import close, close_far


def test_close_positive() -> None:
    for i in [-1, 0, 1, 2, -2]:
        is_close = close(point=1, num=i)
        assert is_close is True


def test_close_negative() -> None:
    for i in [3, 4, 5, -3, -6]:
        is_close = close(point=i, num=i + 2)
        assert is_close is False


def test_close_far() -> None:
    test_cases = [[1, 2, 10], [1, 2, 3], [4, 1, 3], [4, 5, 3], [4, 3, 5], [8, 9, 7]]
    test_cases_ans = [True, False, True, False, False, False]
    for i in range(0, len(test_cases_ans)):
        assert (
            close_far(test_cases[i][0], test_cases[i][1], test_cases[i][2])
            is test_cases_ans[i]
        )
