# @algorithm @lc id=383 lang=python3
# @title ransom-note
from en.Python3.mod.preImport import *
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        for k, v in ransom_counts.items():
            if v > magazine_counts.get(k, 0):
                return False
        return True