# @algorithm @lc id=48 lang=python3
# @title rotate-image
from en.Python3.mod.preImport import *
from math import ceil
class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    n = len(matrix)
    
    def swap_pop(y, x, v):
        yt, xt = x, n-y-1
        t = matrix[yt][xt]
        matrix[yt][xt] = v
        return yt, xt, t
    
    # fast ceiling
    width = -(n // -2)
    height = n // 2 
    for y in range(height):
        for x in range(width):
            yt, xt, t = y, x, matrix[y][x]
            for _ in range(4):
                yt, xt, t = swap_pop(yt, xt, t)