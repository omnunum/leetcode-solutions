
#
# @lc app=leetcode id=4 lang='python3'
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
        
class Solution:
    def sort_zip(self, left, right):
        ln, rn = len(left), len(right)
        li, ri, i = 0, 0, 0
        # if still within respective bounds
        while li < ln and ri < rn:
            if left[li] < right[ri]:
                yield i, left[li]
                li += 1
                i += 1
            else:
                yield i, right[ri]
                ri += 1
                i += 1
        # only one will have entries
        for n in right[ri:] + left[li:]:
            yield i, n
            i += 1

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        mn = len(nums1) + len(nums2)
        indexes = (
            [(mn - 1)//2, mn//2] 
            if mn % 2 == 0 
            else [mn//2]
        )
        
#         if mn % 2 == 0:
#             return sum(sorted(nums1+nums2)[(mn - 1)//2: mn//2 + 1]) / 2
#         else:
#             return sorted(nums1+nums2)[mn//2]
        
        targets = []
        for i, n in self.sort_zip(nums1, nums2):
            if i == indexes[0]:
                indexes.pop(0)
                targets.append(n)
            if not indexes:
                return sum(targets) / len(targets)
# @lc code=end