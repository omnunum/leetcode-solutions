# @algorithm @lc id=1813 lang=python3
# @title maximum-erasure-value
from en.Python3.mod.preImport import *
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        lower = upper = 0 
        total = curr_sum = nums[0]
        limit = len(nums) - 1
        submap = {nums[0]: 0}
        
        while upper < limit:
            upper += 1
            if (n := nums[upper]) not in submap:
                submap[n] = upper
                curr_sum += n
            else:
                old_lower = lower
                lower = submap[n] + 1
                
                for remove in nums[old_lower: lower]:
                    del submap[remove]
                    curr_sum -= remove
                    
                submap[n] = upper
                curr_sum += n
                
            total = max(total, curr_sum)
        return total
