# @algorithm @lc id=11 lang=python3
# @title container-with-most-water
from en.Python3.mod.preImport import *
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
            
                
            