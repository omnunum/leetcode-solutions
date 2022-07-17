#
# @lc app=leetcode id=678 lang='python3'
#
# [678] Valid Parenthesis String
#

# @lc code=start
from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
#         # top down memoize brute force
#         @cache
#         def go(open_paren: int, i: int) -> bool:
#             if i == n:
#                 return not open_paren
            
#             match s[i]:
#                 case "*":
#                     return True if (
#                         go(open_paren + 1, i+1) 
#                         or (open_paren and go(open_paren - 1, i+1))
#                         or go(open_paren, i+1)
#                     ) else False
#                 case "(":
#                     open_paren += 1
#                 case ")":
#                     if open_paren:
#                         open_paren -= 1
#                     else:
#                         return False
#             return go(open_paren, i+1)
#         return go(0, 0)
    
        # range of decisions
        lo = hi = 0
        for c in s:
            match c:
                case "*":
                    lo, hi = lo-1, hi+1
                case "(":
                    lo, hi = lo+1, hi+1
                case ")":
                    lo, hi = lo-1, hi-1
            if hi < 0: return False
            lo = max(0, lo)
        return lo == 0
        
        
        
                
# @lc code=end