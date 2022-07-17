#
# @lc app=leetcode id=42 lang='python3'
#
# [42] Trapping Rain Water
#

# @lc code=start
from collections import Counter
class Solution:
    def trap(self, height: list[int], recurse=True) -> int:
        n = len(height)
        if n == 0:
            return 0
        li = 0

        
        vol = 0
        ri = li + 1
        # need 3 squares to make a bucket
        l = height[li]
        bucket = 0
        while li < n - 2:
            # if we reached the end,we hit maximum and need to scan
            # the rest backwards
            if ri == n:
                if recurse:
                    neg_l = -1 * ((n - li) + 1)
                    subset = height[-1:neg_l:-1]
                    vol += self.trap(subset, recurse=False)
                    break
                else:
                    break
            # if we reached an equal or higher point to li
            # then calculate the vol and bring li to where ri is
            elif (r := height[ri]) >= l:
                vol += bucket
                l, li = r, ri
                ri += 1
                bucket = 0
            # otherwise assume we'll hit a new high and add volume
            # even if throw this out later
            else:
                bucket += l - r
                ri += 1
        return vol
# @lc code=end