
#
# @lc app=leetcode id=20 lang='python3'
#
# [20] Valid Parentheses
#

# @lc code=start
        
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
# @lc code=end