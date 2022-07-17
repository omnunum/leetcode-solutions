#
# @lc app=leetcode id=200 lang='python3'
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def neighbors(i, j):
            for di, dj in ((-1,0), (0, 1), (1, 0), (0, -1)):
                if 0 <= i + di < m and 0 <= j + dj < n:
                    yield i + di, j + dj
                    
        def visit(i, j):
            grid[i][j] = None
            for ni, nj in neighbors(i,j):
                if grid[ni][nj] == "1":
                    visit(ni, nj)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    visit(i,j)                  
        return count
                    
                
# @lc code=end