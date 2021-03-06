# @algorithm @lc id=278 lang=python3
# @title first-bad-version
from en.Python3.mod.preImport import *
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid = n // 2
        highest_good, lowest_bad = 0, n
        while lowest_bad != highest_good + 1:
            if isBadVersion(mid):
                lowest_bad = mid
                mid = (highest_good + mid) // 2
            else:
                highest_good = mid
                mid = (lowest_bad + mid) // 2
        return lowest_bad
            