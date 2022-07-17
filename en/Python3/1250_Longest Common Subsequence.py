# @algorithm @lc id=1250 lang=python3
# @title longest-common-subsequence
from en.Python3.mod.preImport import *
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # prepopulate 2D array of combinations adding an extra
        # row and column that will hold init value
        g = [[0]*(n+1) for _ in range(m+1)]
        
        # iterate through all options, offset by one since
        # the first row and column need to stay 0 (initial value)
        for i in range(1, m+1):
            for j in range(1, n+1):
                # Check if the combination of letters match.
                # The indeces we're using are offset, so they 
                # need to be de-ofsetted when accessing base arrays
                if text1[j-1] == text2[i-1]:
                    # add one to the neg offset diagonal in the grid
                    g[i][j] = g[i-1][j-1] + 1
                else:
                    # grab the max of the neg offset horiz and vert
                    g[i][j] = g[i][j-1] if g[i][j-1] > g[i-1][j] else g[i-1][j]
        return g[m][n]
                