from codingbat.List_2.centered_average import average_of_list, centered_average


def test_cal_average() -> None:
    assert average_of_list([1, 2, 3, 4]) == 10 / 4
    assert average_of_list([-5, 5, 10, 2]) == 3


def test_cen_aver() -> None:
    assert centered_average([1, 2, 3, 4, 100]) == 3
    assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
    assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
