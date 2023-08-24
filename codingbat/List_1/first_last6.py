# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
    return 6 == nums[0] or 6 == nums[len(nums) - 1]
