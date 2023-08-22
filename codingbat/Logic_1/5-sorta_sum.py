# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
def sorta_sum(a, b):
    list_sum = a + b
    if list_sum in range(10, 20):
        return 20
    else:
        return list_sum
