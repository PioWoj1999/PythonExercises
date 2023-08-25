# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


def main():
    return None


def count_evens(nums: list) -> int:
    """
    Function to calculate number of evens number in passed list.
    """
    countEven = 0
    for i in nums:
        if i % 2 == 0:
            countEven += 1
    return countEven


if __name__ == "__main__":
    print(count_evens([2, 1, 2, 3, 4]))
