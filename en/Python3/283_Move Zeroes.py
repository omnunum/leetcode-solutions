# @algorithm @lc id=283 lang=python3
# @title move-zeroes
from en.Python3.mod.preImport import *
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i] == 0:
                nums.insert(l, nums.pop(i))