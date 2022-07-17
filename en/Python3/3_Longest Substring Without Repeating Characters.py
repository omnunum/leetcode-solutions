# @algorithm @lc id=3 lang=python3
# @title longest-substring-without-repeating-characters
from en.Python3.mod.preImport import *
class Solution:
    # edvdfi
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        indexes = {}
        left = 0
        for i, c in enumerate(s):
            if (ci := indexes.get(c, None)) is None:
                current += 1
            else:
                left = max(left, ci + 1)
                current = (i - left) + 1
            longest = max(longest, current)
            indexes[c] = i
        return longest