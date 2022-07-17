# @algorithm @lc id=7 lang=python3
# @title reverse-integer
from en.Python3.mod.preImport import *
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
            
            
        