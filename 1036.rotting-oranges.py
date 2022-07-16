
#
# @lc app=leetcode id=1036 lang='python3'
#
# [1036] Rotting Oranges
#

# @lc code=start
        
# scan through matrix
# each time orange found
    # add to counted, add to visited
    # check 4 direction neighbors
    # visit and track depth
from itertools import product
from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        counted, visited, max_depth = 0, 0, 0
        
        def neighbors(i, j):
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if 0 <= di + i < m and 0 <= dj + j < n:
                    yield di + i, dj + j

        unvisited = deque()
        for (i, j) in product(range(m), range(n)):
            c = grid[i][j] 
            if c == 0: continue
            if c <= 2: counted += 1
            if c ==  2: unvisited.append((i,j,0))

        while unvisited:
            i, j, d = unvisited.popleft()
            max_depth = max(d, max_depth)
            visited += 1
            for ni, nj in neighbors(i, j):
                c = grid[ni][nj]
                if c == 0: continue
                if c == 1: 
                    grid[ni][nj] = 0
                    unvisited.append((ni,nj,d+1))

        return max_depth if counted == visited else -1 
# @lc code=end