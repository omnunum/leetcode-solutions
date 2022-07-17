# @algorithm @lc id=1528 lang=python3
# @title kids-with-the-greatest-number-of-candies
from en.Python3.mod.preImport import *
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        most = max(candies)
        return [(extraCandies >= most - c) for c in candies]
                   