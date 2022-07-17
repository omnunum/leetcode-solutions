#
# @lc app=leetcode id=36 lang='python3'
#
# [36] Valid Sudoku
#

# @lc code=start
# iterte through each cell, if current cells value has been in the same col row or section then fail
from itertools import product
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = defaultdict(lambda: set())
        for i, j in product(range(9), range(9)):
            if (c := board[i][j]) == ".":
                continue
            rules = {("r", i), ("c", j), ("s", (i//3, j//3))}
            if rules & seen[c]: 
                return False
            seen[c] |= rules
        return True
# @lc code=end