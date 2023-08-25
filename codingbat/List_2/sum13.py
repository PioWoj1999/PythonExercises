# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def main():
    return None


def sum13(nums: list) -> int:
    """
    Sum all numbers without 13 and following a 13.
    """
    sumNums, i = 0, 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        else:
            sumNums += nums[i]
            i += 1
    return sumNums


if __name__ == "__main__":
    print(sum13([13, 1, 2, 13, 2, 1, 13]))
