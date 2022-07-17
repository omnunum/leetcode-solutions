#
# @lc app=leetcode id=49 lang='python3'
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grams = defaultdict(list)
        for s in strs:
            grams["".join(sorted(s))].append(s)
        return grams.values()
        
# @lc code=end