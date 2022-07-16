
#
# @lc app=leetcode id=53 lang='python3'
#
# [53] Maximum Subarray
#

# @lc code=start
        
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        highest_sum = nums[0]
        current_sum = nums[0]
        for ri in range(1, len(nums)):
            n = nums[ri]
            if current_sum < 0:
                current_sum = n
            else:
                current_sum += n
            if current_sum > highest_sum:
                highest_sum = current_sum
        return highest_sum

# @lc code=end