# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    if len(nums) < 3:
        return False
    for i in range(0, len(nums) - 2):
        if 1 == nums[i] and 2 == nums[i + 1] and 3 == nums[i + 2]:
            return True
    return False
