# @algorithm @lc id=1603 lang=python3
# @title running-sum-of-1d-array
from en.Python3.mod.preImport import *
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
        