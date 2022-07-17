#
# @lc app=leetcode id=295 lang='python3'
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import * 
# Are stream items unique
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heappush(self.left, -num)
            n = -heappop(self.left)
            heappush(self.right, n)
        else:
            heappush(self.right, num)
            n = heappop(self.right)
            heappush(self.left, -n)
        
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        else:
            return self.right[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# [1, 4, 5, 7, 9]
# 1 -> 2.5 -> 4 -> 4.5 -> 5

# [1, 7, 4, 9, 5]
# 1 -> 4 -> 4 -> 5.5 -> 5

# [] 1 []
# [1] [4, 7]
# @lc code=end