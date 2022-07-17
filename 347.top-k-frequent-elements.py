#
# @lc app=leetcode id=347 lang='python3'
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        top = heapq.nlargest(k, counter.items(), key=lambda x: x[1])
        return [x[0] for x in top]
# @lc code=end