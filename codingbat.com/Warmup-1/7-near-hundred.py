# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
    if n < 0:
        return False
    elif abs(100 - n) in range(0, 11) or abs(200 - n) in range(0, 11):
        return True
    else:
        return False
