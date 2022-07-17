# @algorithm @lc id=1737 lang=python3
# @title maximum-nesting-depth-of-the-parentheses
from en.Python3.mod.preImport import *
class Solution:
    def maxDepth(self, s: str) -> int:
        max_opens = 0
        opens = 0
        for n in s:
            if n == '(':
                opens += 1
                max_opens = max(max_opens, opens)
            elif n == ')':
                opens -= 1
        return max_opens