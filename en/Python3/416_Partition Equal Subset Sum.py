# @algorithm @lc id=416 lang=python3 
# @title partition-equal-subset-sum


from en.Python3.mod.preImport import *
# @test([1,5,11,5])=true
# @test([1,2,3,5])=false
from functools import cache
class Solution:
    # TODO: Improve efficiency
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def go(i: int, left_sum: int, right_sum: int) -> bool:
            if i == n:
                return left_sum == right_sum
            # optimize call stack by choosing targeted order
            if left_sum < right_sum:
                if go(i+1, left_sum+nums[i], right_sum):
                    return True
                if go(i+1, left_sum, right_sum+nums[i]):
                    return True
            else:
                if go(i+1, left_sum, right_sum+nums[i]):
                    return True
                if go(i+1, left_sum+nums[i], right_sum):
                    return True
            return False
        return go(0, 0, 0)
    