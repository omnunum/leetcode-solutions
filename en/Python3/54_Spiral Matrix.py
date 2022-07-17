# @algorithm @lc id=54 lang=python3
# @title spiral-matrix
from en.Python3.mod.preImport import *
from itertools import cycle
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        dy, dx = next(directions)
        m, n = len(matrix), len(matrix[0])
        output = []
        y, x = 0, 0
        
        def needs_to_turn(y: int, x: int) -> int:
            # check if we're within bounds
            out_bounds = not (0 <= y < m and 0 <= x < n)
            # if we are then check if we've been here already
            return out_bounds or matrix[y][x] is None
        
        while True:
            # if we need to turn at the current cell
            # then we already hit the last valid cell
            if needs_to_turn(y, x):
                return output
            
            # otherwise add this cell to output and mark seen
            output.append(matrix[y][x])  
            matrix[y][x] = None
                
            # if we've been to the next cell already
            if needs_to_turn(y+dy, x+dx):
                # turn 90 degrees
                dy, dx = next(directions)
                
            # move to next cell
            y, x = y+dy, x+dx
            
            