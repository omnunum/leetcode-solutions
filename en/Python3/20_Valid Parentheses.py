# @algorithm @lc id=20 lang=python3
# @title valid-parentheses
from en.Python3.mod.preImport import *
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        bs = ""
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for b in s:
            if b not in mapping:
                bs += b
            elif bs[-1:] == mapping[b]:
                bs = bs[:-1]
            else:
                return False
        return not bool(bs)