
#
# @lc app=leetcode id=860 lang='python3'
#
# [860] Design Circular Queue
#

# @lc code=start
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.q = [None] * k
        self.rear, self.front = -1, 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.q[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.q[self.front] if self.size else -1

    def Rear(self) -> int:
        return self.q[self.rear] if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size >= self.max_size

# # Deque based
#     from collections import deque
#     def __init__(self, k: int):
#         self.q = deque([])
#         self.max_size = k

#     def enQueue(self, value: int) -> bool:
#         if len(self.q) == self.max_size:
#             return False
#         self.q.appendleft(value)
#         return True
    
#     def deQueue(self) -> bool:
#         if len(self.q) == 0:
#             return False
#         self.q.pop()
#         return True

#     def Front(self) -> int:
#         return self.q[-1] if len(self.q) else -1

#     def Rear(self) -> int:
#         return self.q[0] if len(self.q) else -1

#     def isEmpty(self) -> bool:
#         return len(self.q) == 0

#     def isFull(self) -> bool:
#         return len(self.q) == self.max_size



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end