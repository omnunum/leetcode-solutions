
#
# @lc app=leetcode id=139 lang='python3'
#
# [139] Word Break
#

# @lc code=start
        
# S(l, r) = max(
#   -- expand existing word    
#   max(r, S(l, r+1)), 
#.  -- start new word
#.  max(r, S(r+1, r+2))
# ) 
from functools import cache
class Solution:
    
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        if n == 1:
            return s in wordDict
        
        # Top down memo
        @cache
        def word_search(to_build: str) -> bool:
            if to_build == "":
                return True
            for word in wordDict:
                if not to_build.startswith(word):
                    continue
                if word_search(to_build[len(word):]):
                    return True
            return False
        
        return word_search(s)

        
        
# @lc code=end