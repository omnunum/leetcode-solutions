# @algorithm @lc id=49 lang=python3
# @title group-anagrams
from en.Python3.mod.preImport import *
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grams = defaultdict(list)
        for s in strs:
            grams["".join(sorted(s))].append(s)
        return grams.values()
        