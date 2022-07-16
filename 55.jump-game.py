
#
# @lc app=leetcode id=55 lang='python3'
#
# [55] Jump Game
#

# @lc code=start
        
class Solution:    
    def canJump(self, nums: list[int]) -> bool:
        n, curr, prev = len(nums) - 1, 0, 0
        if n == 0:
            return True
        if nums[0] == 0 and n > 1:
            return False
        
        while True:
            # jump forward until we hit a zero
            while nums[curr] > 0:
                prev = curr
                curr += nums[curr]
                if curr >= n:
                    return True
            # then find the number of steps we need
            # to go until we hit a non-zero from here
            needs_to_jump = 0
            while (
                curr + needs_to_jump < n 
                and nums[curr + needs_to_jump] == 0
            ):
                needs_to_jump += 1
            # track backwards until we hit a number thats
            # higher than the amount we need to hit to get
            # a non zero, incrementing the amount as we go
            while nums[curr] < needs_to_jump:
                # no possible higher number than 9 so fail early
                if needs_to_jump == 9:
                    return False
                curr -= 1
                needs_to_jump += 1
                # had to go past the first number so fail late
                if curr < 0:
                    return False
# @lc code=end