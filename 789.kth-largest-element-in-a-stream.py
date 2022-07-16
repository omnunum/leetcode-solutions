
#
# @lc app=leetcode id=789 lang='python3'
#
# [789] Kth Largest Element in a Stream
#

# @lc code=start
        
# T = 15min
import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        n = len(nums)
        self.k = k
        self.nums = sorted(nums)[max(n-k, 0):]
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val >= self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end