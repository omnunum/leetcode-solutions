# @algorithm @lc id=1791 lang=python3
# @title richest-customer-wealth
from en.Python3.mod.preImport import *
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(w) for w in accounts])