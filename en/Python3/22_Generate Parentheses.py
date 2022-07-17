# @algorithm @lc id=22 lang=python3
# @title generate-parentheses
from en.Python3.mod.preImport import *
from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parens = []
        q = deque([('(', n-1, n)])
        while q:
            s, o, c = q.pop()
            if o == c == 0:
                parens.append(s)
                continue
            if o > 0:
                q.append((s+'(', o-1, c))
            if c > o >= 0:
                q.append((s+')', o, c-1))
                
        return parens
            