#
# @lc app=leetcode id=14 lang='python3'
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        confirmed = ""
        pos = 0
        while True:
            possible = strs[0][pos:pos+1]
            for word in strs:
                if pos == len(word) or possible != word[pos]:
                     return confirmed
            confirmed += possible
            pos += 1
                    
                
# @lc code=end