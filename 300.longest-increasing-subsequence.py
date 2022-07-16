
#
# @lc app=leetcode id=300 lang='python3'
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
        
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        q = [nums[0]]
        for n in nums[1:]:
            if q[-1] < n:
                q.append(n)
            else:
                i = bisect_left(q, n)
                q[i] = n
        return len(q)
            
# @lc code=end