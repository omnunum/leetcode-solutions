
#
# @lc app=leetcode id=7 lang='python3'
#
# [7] Reverse Integer
#

# @lc code=start
        
class Solution:
    def reverse(self, x: int) -> int:
        flip = (x < 0)
        num = 0
        x = abs(x)
        while x:
            div, mod = divmod(x, 10)
            if num == 0:
                num = mod
            else:
                num = (num * 10) + mod
            x = div
        if num >= (-1 * 2**31) and num <= (2**31 - 1):
            return num * -1 if flip else num
        else:
            return 0
            
            
        
# @lc code=end