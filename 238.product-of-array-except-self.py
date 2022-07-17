#
# @lc app=leetcode id=238 lang='python3'
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        right = []
        
        t = 1
        # build list going backwards, then flip
        # faster than insert(0,n)
        for i in range(len(nums)-1, -1, -1):
            t *= nums[i]
            right.append(t)
        right = right[::-1]
            
        l = nums[0]
        for i in range(len(nums)):
            if i == 0:
                right[i] = right[i + 1]
            elif i == len(nums) - 1:
                right[i] = l
            else:
                l, right[i] = l * nums[i], l * right[i + 1]
                
            
        return right

# @lc code=end