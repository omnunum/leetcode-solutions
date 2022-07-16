
#
# @lc app=leetcode id=11 lang='python3'
#
# [11] Container With Most Water
#

# @lc code=start
        
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        maxi = 0
        li, ri = 0, n - 1
        while li < ri:
            l, r = height[li], height[ri]
            d, h = ri - li, min(l, r)
            maxi = max(maxi, h*d)
            if l <= r:
                li += 1
            else:
                ri -= 1
        return maxi
            
                
            
# @lc code=end