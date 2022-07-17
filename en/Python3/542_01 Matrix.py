# @algorithm @lc id=542 lang=python3
# @title 01-matrix
from en.Python3.mod.preImport import *
from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # make function to get neighbors
        # check if distance already calculated for nearby panel
        #  if so, take min of neoghbors and +1
        #  else BFS to find panel
        y_len, x_len = len(mat) - 1, len(mat[0]) - 1
        
        def neighbors(y, x, m):
            if not m:
                return
            for xd, yd in ((0,1), (0,-1), (1,0), (-1,0)):
                x_bounds = 0 <= x+xd <= x_len
                y_bounds = 0 <= y+yd <= y_len
                if not x_bounds or not y_bounds:
                    continue
                yield yd, xd
        
        # populate distances and find zeros
        distances, zero_locs = [], []
        for y, row in enumerate(mat):
            d_row = []
            for x, cell in enumerate(row):
                if cell == 0:
                    d_row.append(0)
                    zero_locs.append((y, x, 0))
                else:
                    d_row.append(float("inf"))
            distances.append(d_row)
            
        # BFS starting with all zero locations
        q = deque(zero_locs)
        while q:
            y, x, depth = q.popleft()
            for yd, xd in neighbors(y,x,mat):
                update_depth = (
                    mat[y+yd][x+xd] == 1 
                    and depth+1 < distances[y+yd][x+xd]
                )
                if update_depth:
                    distances[y+yd][x+xd] = depth+1
                    q.append((y+yd, x+xd, depth+1))
                  
        return distances