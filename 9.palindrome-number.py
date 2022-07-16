
#
# @lc app=leetcode id=9 lang='python3'
#
# [9] Palindrome Number
#

# @lc code=start
        
import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x < 0:
            return False

        reverse = 0

        while x > 0:
            reverse = (10*reverse) + x % 10
            x //= 10

        return reverse == original
# @lc code=end