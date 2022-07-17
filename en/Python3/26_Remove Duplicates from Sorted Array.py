# @algorithm @lc id=26 lang=python3
# @title remove-duplicates-from-sorted-array
from en.Python3.mod.preImport import *
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        i = 0
        while nums[i:i+2] != nums[i:i+1]:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return i + 1
            
            