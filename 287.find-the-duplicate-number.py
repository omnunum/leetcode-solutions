
#
# @lc app=leetcode id=287 lang='python3'
#
# [287] Find the Duplicate Number
#

# @lc code=start
        
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # use slow-fast pointers to detect cycle
        # starting at the head
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        # reset fast pointer and set it to the head
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
                
        return slow
# @lc code=end