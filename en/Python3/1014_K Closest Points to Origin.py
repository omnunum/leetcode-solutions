# @algorithm @lc id=1014 lang=python3
# @title k-closest-points-to-origin
from en.Python3.mod.preImport import *
# T = 10 min
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        q = []
        for p in points:
            d = (p[0]*p[0] + p[1]*p[1])
            if len(q) < k:
                heapq.heappush(q, (-d, p))
            else:
                heapq.heappushpop(q, (-d, p))
        return [p[1] for p in q]