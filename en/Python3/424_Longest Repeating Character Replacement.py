# @algorithm @lc id=424 lang=python3
# @title longest-repeating-character-replacement
from en.Python3.mod.preImport import *
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        li = 0
        n = len(s)
        freq = defaultdict(int) # frequency of chars in window
        maxf = 0 # count of the most common character inside of the window
        maxd = 0 # max window size seen
        
        # move window to the right and use the left pointer to
        # "catch up" when we go outside of the (k + maxc) constraint
        for ri in range(n):
            r, l = s[ri], s[li]
            
            # add to the counter for this char, save if new max
            freq[r] += 1
            if freq[r] > maxf:
                maxf = freq[r]
            
            # d is measurement of how many chars are in the window
            # we subtract the amount of the most frequently occuring
            # character in the window because those are "free" and don't
            # count towards k, since only replacements count as k
            while (d := ri - li + 1) - maxf > k:
                # while we fail the constraints, "catch up"
                # until we pass, by bringing the left index
                # towards the right index, making the window smaller
                # reduce the freq count of each char as we move
                freq[l] -= 1
                li += 1
                
            # if window size d is greater than previous max
            if d > maxd:
                maxd = d
        return maxd
            