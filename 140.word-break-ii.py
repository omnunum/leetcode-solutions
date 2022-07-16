
#
# @lc app=leetcode id=140 lang='python3'
#
# [140] Word Break II
#

# @lc code=start
        
# iterate through wordDict
# check if s begins with word
# if yes then split s into prefix and suffix
# pass on suffix into recursive call
# if call returns a string, append each string (with a space)
# to the current prefix and add to solutions list
# when wordDict dont iterating return solutions list
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        @cache
        def construct(search: str) -> str:
            # base case to exit when bottom of tree
            if search == "":
                return [""]
            
            solutions = []
            for word in wordDict:
                if not search.startswith(word):
                    continue
                prefix, suffix = word, search[len(word):]
                if (downstream_solutions := construct(suffix)) is not []:
                    for ds in downstream_solutions:
                        solutions.append(prefix + " " + ds)
            return solutions
        
        # strip off the base cases that add an extra space
        return [s.strip() for s in construct(s)]
# @lc code=end