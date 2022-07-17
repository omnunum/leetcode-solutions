#
# @lc app=leetcode id=150 lang='python3'
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from operator import add, sub, mul
from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        buffer = tokens
        operators = {
            "+": add , 
            "-": sub, 
            "/": lambda x, y: int(x/y), 
            "*": mul
        } 
        i = 0
        while len(buffer) > 1:
            t = buffer[i]
            if not t in operators:
                buffer[i] = int(t)
                i += 1
                continue
            operator = buffer.pop(i)
            right_operand = buffer.pop(i-1)
            left_operand = buffer.pop(i-2)
            operation = operators[operator]
            result = operation(left_operand, right_operand)
            buffer.insert(i-2, result)
            i -= 1
        return buffer[0]
            
# @lc code=end