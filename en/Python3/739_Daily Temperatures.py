# @algorithm @lc id=739 lang=python3
# @title daily-temperatures
from en.Python3.mod.preImport import *
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0]*len(temperatures)
        lookup = [float("inf")]*71
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            ti = t-30
            lookup[ti] = i
            if not (remainder := lookup[ti+1:]):
                continue
            if (nearest := min(remainder)) != float("inf"):
                output[i] = nearest - i
        return output