# @algorithm @lc id=322 lang=python3
# @title coin-change
from en.Python3.mod.preImport import *
class Solution:
    from functools import cache
    def coinChange(self, A: list[int], T: int) -> int:
        INF = float("inf")
        n = len(A)

        @cache
        def go(i: int, T: int) -> int:
            if T == 0:
                return 0
            if i == n:
                return INF
            repeat = go(i, T - A[i]) + 1 if T - A[i] >= 0 else INF
            move = go(i+1, T)
            return min(repeat, move)
        
        A.sort(reverse=True)
        count = go(0, T)
        return count if count != INF else -1
