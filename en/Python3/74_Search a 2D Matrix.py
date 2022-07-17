# @algorithm @lc id=74 lang=python3
# @title search-a-2d-matrix
from en.Python3.mod.preImport import *
from math import ceil
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_search_closest(nums: list[int], target: int) -> int:
            n = len(nums)
            li, ri = 0, n - 1
            while li != (mi := (ri + li) // 2) != ri:
                if nums[mi] > target:
                    ri = mi
                elif nums[mi] < target:
                    li = mi
                else:
                    return mi
            
            return li if target < nums[ri] else ri
                
        row = binary_search_closest([r[0] for r in matrix], target)
        col = binary_search_closest(matrix[row], target)
        return target == matrix[row][col]
        