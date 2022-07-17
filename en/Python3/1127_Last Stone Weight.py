# @algorithm @lc id=1127 lang=python3
# @title last-stone-weight
from en.Python3.mod.preImport import *
import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x == y:
                continue
            heapq.heappush(stones, -(x - y))
        return -stones[0] if stones else 0
            