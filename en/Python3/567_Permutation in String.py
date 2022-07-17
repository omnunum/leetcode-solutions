# @algorithm @lc id=567 lang=python3
# @title permutation-in-string
from en.Python3.mod.preImport import *
from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        target_freq = Counter(s1)
        freq = defaultdict(int)
        ri, li = 0, 0
        
        while ri < n:
            freq[s2[ri]] += 1
            ri += 1
            if freq == target_freq:
                return True
            # if window has hit max length, then shift left forward
            # and decrement that letter
            # if we no longer have any of that letter, remove it entirely
            if (d := ri - li) == m:
                freq[s2[li]] -= 1
                if freq[s2[li]] == 0:
                    del freq[s2[li]]
                li += 1
            
        return False