# @algorithm @lc id=57 lang=python3
# @title insert-interval
from en.Python3.mod.preImport import *
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:        
        s, e = newInterval
        left, right = [], []
        for l, r in intervals:
            if s > r:
                left.append([l,r])
            elif e < l:
                right.append([l,r])
            else:
                s = min(l, s)
                e = max(r, e)
        return left + [[s,e]] + right
            
                    
                
                
                