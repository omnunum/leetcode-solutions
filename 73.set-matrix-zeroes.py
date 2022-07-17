#
# @lc app=leetcode id=73 lang='python3'
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        cols = set()
        
        for y in range(m):
            found = False
            for x in range(n):
                if matrix[y][x] == 0:
                    found = True
                    cols.add(x)
            if found:
                matrix[y] = [0] * n
        
        for y in range(m):
            for x in range(n):
                if x in cols:
                    matrix[y][x] = 0
        
        
# @lc code=end