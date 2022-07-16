
#
# @lc app=leetcode id=155 lang='python3'
#
# [155] Min Stack
#

# @lc code=start
        
class MinStack:

    def __init__(self):
        self._stack = []
        self._min = None
        self._top = None

    def push(self, val: int) -> None:
        if self._top is not None:
            self._stack.append(self._top)
        self._top = val
        if self._min is None:
            self._min = val
        self._min = min(val, self._min)

    def pop(self) -> None:
        if (t := self._top) is None:
            return
        
        if self._stack:
            self._top = self._stack.pop()
            if t == self._min:
                self._min = min([self._top] + self._stack)
        else:
            self._top = None
            self._min = None

        return t

    def top(self) -> int:
        return self._top

    def getMin(self) -> int:
        return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end