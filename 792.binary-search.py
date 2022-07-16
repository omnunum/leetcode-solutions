
#
# @lc app=leetcode id=792 lang='python3'
#
# [792] Binary Search
#

# @lc code=start
        
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def split(li, ri):
            if ri - li <= 1:
                return -1
            mi = (ri + li) // 2
            mid = nums[mi]
            if target > mid:
                return split(mi, ri)
            if target < mid:
                return split(li, mi)
            if target == mid:
                return mi
        limit = len(nums) - 1
        if target == nums[0]:
            return 0
        elif target == nums[limit]:
            return limit
        return split(0, limit)
            
# @lc code=end