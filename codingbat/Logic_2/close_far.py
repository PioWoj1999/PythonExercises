# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
    if (
        (close(point=a, num=b) is True and close(point=a, num=c) is False)
        or close(point=a, num=c) is True
        and close(point=a, num=b) is False
        # and close(b, c) is False
    ) and close(b, c) is False:
        return True
    else:
        return False


def close(point, num):
    """
    Calculate if number is close to 1.
    """
    if abs(point - abs(num)) <= 1:
        return True
    else:
        return False
