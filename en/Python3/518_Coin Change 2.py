# @algorithm @lc id=518 lang=python3 
# @title coin-change-2


from en.Python3.mod.preImport import *
# @test(5,[1,2,5])=4
# @test(3,[2])=0
# @test(10,[10])=1
from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        @cache
        def go(i: int, remainder: int) -> int:
            if remainder == 0:
                return 1
            if remainder < 0:
                return 0
            if i == n:
                return 0
            same = go(i, remainder - coins[i])
            nxt = go(i+1, remainder)
            return same + nxt
        return go(0, amount)
                 