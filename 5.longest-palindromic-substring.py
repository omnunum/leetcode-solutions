
#
# @lc app=leetcode id=5 lang='python3'
#
# [5] Longest Palindromic Substring
#

# @lc code=start
        
# True if 
    # even len and first half is same as inverse order second half
    # odd len and first half floored is same as that + 1 to end inverted
# "oiuyu0asdfdsa0werty0mnbvcxxcvbnm"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = s[0]
        def longer(l, r):
            return l if len(r) < len(l) else r
        for i in range(0, len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest = longer(longest, s[l:r+1])
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest = longer(longest, s[l:r+1])
                l -= 1
                r += 1
                
        return longest
# @lc code=end