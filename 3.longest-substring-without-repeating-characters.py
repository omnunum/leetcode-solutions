#
# @lc app=leetcode id=3 lang='python3'
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
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
# @lc code=end