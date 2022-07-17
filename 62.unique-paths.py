#
# @lc app=leetcode id=62 lang='python3'
#
# [62] Unique Paths
#

# @lc code=start
from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # explanation https://math.stackexchange.com/questions/2486807/
        from math import factorial as f
        # number of combinations formula
        # nCk = n! / k!(n - k)!
        
        # number of total moves
        # starting from origin, we will make 6 moves to the right
        # which is one less than the horizontal (m) size of the grid
        # and 2 moves downward, so size is (m - 1) + (n - 1) = (m + n - 2)
        total = m + n - 2
        # number of choices we will have for each combination
        # is the number of times we move down, since we're
        # otherwise assuming we are moving rightf
        size = m - 1
        
        #using above formula for combinations
        combs = f(total) / (f(size) * f(total - size))
        return int(combs)
    
# T = 20
# Binary Decision tree with Memoization (dynamic programming)
#     @cache
#     def seek(self, i: int, j: int) -> int:
#         if i == self.m - 1 and j == self.n - 1:
#             return 1
#         right_paths, down_paths = 0, 0
#         if j < self.n - 1:
#             right_paths = self.seek(i, j + 1)
#         if i < self.m - 1:
#             down_paths = self.seek(i + 1, j)
#         return right_paths + down_paths
        
#     def uniquePaths(self, m: int, n: int) -> int:
#         self.m, self.n = m, n
#         return self.seek(0, 0)
# @lc code=end