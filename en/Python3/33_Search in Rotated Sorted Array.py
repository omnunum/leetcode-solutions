# @algorithm @lc id=33 lang=python3
# @title search-in-rotated-sorted-array
from en.Python3.mod.preImport import *
# [4,5,6,7,0,1,2] -> [0,1,2,4,5,6,7]
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # If the last number is less than the first one
        # we have a shifted array, since we know the numbers
        # we sorted ascending before the optinal shift.
        # We need to binary search through the array looking for 
        # the index where the left is greater than the middle/right
        if (shifted := nums[-1] < nums[0]):
            li, ri = 0, n - 1
            while li < ri - 1:
                mi = (li + ri) // 2
                if nums[mi] > nums[ri]:
                    li = mi
                elif nums[mi] < nums[li]:
                    ri = mi
            # take the distance that the end of the ascending portion
            # of the index is from the last element
            shift = n - 1 - li
        else:
            shift = 0
        sorted_index = lambda i: (i + (n - shift)) % n
        # now that we can use the `shift` to translate the 
        # index of the element we're currently looking at
        # to the index of the element in the correct sorting
        # without the shift, we just have to do another
        # binary search for the target.
        #
        # if we wanted to double the memory and use the sorted
        # list it would look like
        # sort = [nums[sorted_index(i)] for i in range(n)]
        li, ri = 0, n - 1
        while li < ri - 1:
            mi = (li + ri) // 2
            smi = sorted_index(mi)
            if (m := nums[smi]) > target:
                ri = mi
            elif m < target:
                li = mi
            else:
                return smi
        sli, sri = sorted_index(li), sorted_index(ri)
        if target == nums[sli]: 
            return sli
        elif target == nums[sri]: 
            return sri
        else:
            return -1
        
        