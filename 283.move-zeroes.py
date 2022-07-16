
#
# @lc app=leetcode id=283 lang='python3'
#
# [283] Move Zeroes
#

# @lc code=start
        
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i] == 0:
                nums.insert(l, nums.pop(i))
# @lc code=end