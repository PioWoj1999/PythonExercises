# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
    return 0


def close(point, num):
    if abs(point - num) <= 1:
        return True
    else:
        return False


# TODO - test cases for close
