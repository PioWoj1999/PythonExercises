# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if negative:
        if a * b > 0 and (a < 0 or b < 0):
            return True
        else:
            return False
    elif a * b < 0:
        return True
    else:
        return False
