#
# @lc app=leetcode id=1603 lang='python3'
#
# [1603] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
        
# @lc code=end