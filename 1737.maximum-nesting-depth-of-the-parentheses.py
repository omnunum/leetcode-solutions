
#
# @lc app=leetcode id=1737 lang='python3'
#
# [1737] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
        
class Solution:
    def maxDepth(self, s: str) -> int:
        max_opens = 0
        opens = 0
        for n in s:
            if n == '(':
                opens += 1
                max_opens = max(max_opens, opens)
            elif n == ')':
                opens -= 1
        return max_opens
# @lc code=end