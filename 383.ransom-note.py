#
# @lc app=leetcode id=383 lang='python3'
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        for k, v in ransom_counts.items():
            if v > magazine_counts.get(k, 0):
                return False
        return True
# @lc code=end