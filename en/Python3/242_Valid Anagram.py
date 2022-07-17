# @algorithm @lc id=242 lang=python3
# @title valid-anagram
from en.Python3.mod.preImport import *
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)