# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
# TODO: practice
def lone_sum(a, b, c):
    arr = [a, b, c]
    listLoneSum = [i for i in arr if arr.count(i) < 2]
    return sum(listLoneSum)
