#
# @lc app=leetcode id=215 lang='python3'
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        return sorted(nums)[-k]
# @lc code=end