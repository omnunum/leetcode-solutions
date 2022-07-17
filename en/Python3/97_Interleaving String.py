# @algorithm @lc id=97 lang=python3
# @title interleaving-string
from en.Python3.mod.preImport import *
from functools import cache
class Solution:
    # naive memoized
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i1, i2, i3 = 0, 0, 0
        n1, n2 = len(s1), len(s2)
        while i3 < len(s3):
            if i1 < n1 and i2 < n2 and s1[i1] == s2[i2] == s3[i3]:
                return (
                    self.isInterleave(s1[i1:], s2[i2+1:], s3[i3+1:])
                    or self.isInterleave(s1[i1+1:], s2[i2:], s3[i3+1:])
                )
            if i1 < n1 and s1[i1] == s3[i3]:
                i1 += 1
                i3 += 1
                continue
            elif i2 < n2 and s2[i2] == s3[i3]:
                i2 += 1
                i3 += 1
                continue
            else:
                return False
        return i1 == n1 and i2 == n2
    
    