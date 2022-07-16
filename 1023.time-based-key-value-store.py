
#
# @lc app=leetcode id=1023 lang='python3'
#
# [1023] Time Based Key-Value Store
#

# @lc code=start
        
from collections import defaultdict
import heapq
""" 
TimeMap = {
    key : heapq[(timestamp, value)]
}
"""
# 1 2 3 4 5 

class TimeMap:

    def __init__(self):
        self._store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not (tvs := self._store[key]):
            return ""
        
        n = len(tvs)
        li, ri = 0, n - 1
        
        # O(1) solutions if timestamp is out of range
        if tvs[ri][0] < timestamp:
            return tvs[ri][1]
        elif tvs[li][0] > timestamp:
            return ""

        # O(log2*n) binary search
        while li != ri:
            mi = -((li + ri) // -2)
            m = tvs[mi]
            if timestamp < m[0]:
                ri = mi - 1
            else:
                li = mi
        
        if tvs[li][0] <= timestamp:
            return tvs[li][1]
        return ""
# @lc code=end