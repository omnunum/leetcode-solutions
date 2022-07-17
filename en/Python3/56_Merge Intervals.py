# @algorithm @lc id=56 lang=python3
# @title merge-intervals
from en.Python3.mod.preImport import *
# Are they sorted on the way in?
# Can we modify in place

# T = 20m

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        stack = [intervals[0]]
        # Keeping track of highest value faster than indexing?
        top = stack[-1]
        for start, end in intervals:
            if start <= top[1]:
                top[1] = max(top[1], end)
            else:
                top = [start,end]
                stack.append(top)
        return stack