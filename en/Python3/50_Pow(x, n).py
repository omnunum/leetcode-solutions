# @algorithm @lc id=50 lang=python3
# @title powx-n
from en.Python3.mod.preImport import *
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int) -> float:
            if n == 0: 
                return 1
            elif n % 2:
                return x * pow(x, n - 1)
            else:
                m = pow(x, n // 2)
                return m * m
            
        return 1/pow(x, abs(n)) if n < 0 else pow(x, n)
