# @algorithm @lc id=794 lang=python3 
# @title swim-in-rising-water


from en.Python3.mod.preImport import *
# @test([[0,2],[1,3]])=3
# @test([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])=16
import heapq
class Solution:
    # TODO: Pass all testcases
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = {(0,0)}
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # max_seen, y, x
        q = [(0, 0, 0)]
        while q:
            max_seen, y, x = heapq.heappop(q)
            seen.add((y,x))
            # set max for this cell
            curr_max = max(max_seen, grid[y][x])
            # no more travelling from here if we've hit the base case
            if (y,x) == (n-1, m-1):
                return curr_max
            for yd, xd in deltas:
                if not (
                    0 <= y+yd < n 
                    and 0 <= x+xd < m
                    and (y+yd,x+xd) not in seen
                ): continue
                heapq.heappush(q, (curr_max, y+yd, x+xd))
        
