"""Given an array length 1 or more of ints, return the difference 
between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the 
smaller or larger of two values."""


def main():
    """
    Main function.
    """
    return None


def big_diff(nums: list) -> int:
    """
    Calculate difference between max and min from list
    """
    return max(nums) - min(nums)


if __name__ == "__main__":
    print(big_diff([1, 2, 3, 4]))
