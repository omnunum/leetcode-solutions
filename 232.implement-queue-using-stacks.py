
#
# @lc app=leetcode id=232 lang='python3'
#
# [232] Implement Queue using Stacks
#

# @lc code=start
        
class MyQueue:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.insert(0, x)

    def pop(self) -> int:
        return self.l.pop()

    def peek(self) -> int:
        return self.l[-1]

    def empty(self) -> bool:
        return self.l == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end