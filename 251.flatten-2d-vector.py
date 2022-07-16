
#
# @lc app=leetcode id=251 lang='python3'
#
# [251] Flatten 2D Vector
#

# @lc code=start
        
class Vector2D:

    def __init__(self, vec: list[list[int]]):
        self.vec = vec
        self.total = sum([len(y) for y in vec])
        self.current = 0
        def gen():
            for y in self.vec:
                for x in y:
                    self.current += 1
                    yield x
        self.gen = gen()
        
    def next(self) -> int:        
        return next(self.gen)
        
    def hasNext(self) -> bool:
        return self.current < self.total


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end