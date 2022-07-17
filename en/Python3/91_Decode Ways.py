# @algorithm @lc id=91 lang=python3
# @title decode-ways
from en.Python3.mod.preImport import *

class Solution:
    #T = 10
    from functools import cache
    @cache
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 1
        
        if s[0] == "0":
            return 0
        
        total_at_level = 0
        if len(s) >= 1:
            total_at_level += self.numDecodings(s[1:])
        if len(s) >= 2 and int(s[:2]) <= 26 :
            total_at_level += self.numDecodings(s[2:])
            
        return total_at_level

    def numDecodings(self, s: str) -> int:
        # We want the number of sequences containing only valid decisions 
        # N = Number of valid sequences
        #   sequence is valid when all decisions are valid
        # Dn = Number of decisions in a sequence
        #   which is in the range of [len(s)/2, len(s)]
        # Time complexity:
        # Brute force: O(2^n)
        # DP: O(2n)
        #
        # Decisions:
        # 1) Is this single digit valid, if so move forward one
        #   1 <= d1 <= 9
        # 2) Are these two digits valid, if so move forward two
        #   10 <= d2 <= 26
        #
        # Necessary State:
        # Previous two digits
        
        # Edge cases
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        # Init state
        dp = deque([], 2)
        
        # Base Conditions
        # we know for sure now that the first digit is valid 
        # due to edge case handling above
        dp.append(1)
        # if next single digit is valid add that too
        if s[1] != 0:
            dp.append(1)
        
        # Now that we have two prior decisions, we can calcuate
        # decisions involving two digits
        for i in range(2, len(s) + 1):
            curr = 0
            if 1 <= int(s[i-1]) <= 9:
                curr += dp[-1]
            if 10 <= int(s[i-2:i]) <= 26:
                curr += dp[-2]
            dp.append(curr)
        return dp[-1]