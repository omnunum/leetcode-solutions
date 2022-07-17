# @algorithm @lc id=347 lang=python3
# @title top-k-frequent-elements
from en.Python3.mod.preImport import *
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        top = heapq.nlargest(k, counter.items(), key=lambda x: x[1])
        return [x[0] for x in top]