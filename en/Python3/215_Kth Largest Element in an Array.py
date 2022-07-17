# @algorithm @lc id=215 lang=python3
# @title kth-largest-element-in-an-array
from en.Python3.mod.preImport import *

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        return sorted(nums)[-k]