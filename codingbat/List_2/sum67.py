# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


def main():
    return None


def sum67(nums: list) -> int:
    """
    Return sum of numbers except ones betwenn 6 and 7 in list.
    """
    sumNums = 0
    remove = False

    for i in nums:
        if i == 6:
            remove = True
            continue
        if i == 7 and remove:
            remove = False
            continue
        if not remove:
            sumNums += i
    return sumNums


if __name__ == "__main__":
    print(sum67([1, 2, 2, 6, 99, 99, 7]))
