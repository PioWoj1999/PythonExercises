from codingbat.Logic_2.no_teen_sum import fix_teen, no_teen_sum


def test_fix_teen_return_number() -> None:
    for i in [15, 16, 20, 10, 12, 22, 38, 10]:
        assert fix_teen(i) == i


def test_fix_teen_0() -> None:
    for i in range(13, 20, 1):
        if i == 15 or i == 16:
            continue
        assert fix_teen(i) == 0


def test_no_teen_sum() -> None:
    ans = [6, 3, 3]
    data = [[1, 2, 3], [2, 13, 1], [2, 1, 14]]
    for i in range(0, len(ans)):
        assert no_teen_sum(data[i][0], data[i][1], data[i][2]) == ans[i]
