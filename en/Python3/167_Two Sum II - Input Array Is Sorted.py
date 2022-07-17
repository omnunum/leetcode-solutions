# @algorithm @lc id=167 lang=python3
# @title two-sum-ii-input-array-is-sorted
from en.Python3.mod.preImport import *

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ns = numbers
        li, ri = 0, len(numbers) - 1
        while (summed := ns[li] + ns[ri]) != target:
            if summed > target:
                ri -= 1
                continue
            if summed < target:
                li += 1
                continue
            
        return [li + 1, ri + 1]