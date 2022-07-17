#
# @lc app=leetcode id=202 lang='python3'
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x)**2 for x in str(n)])
            if n == 1:
                return True
        return False
# @lc code=end