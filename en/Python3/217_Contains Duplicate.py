# @algorithm @lc id=217 lang=python3
# @title contains-duplicate
from en.Python3.mod.preImport import *
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        existing = set()
        for n in nums:
            if n in existing:
                return True
            existing.add(n)
        return False
        