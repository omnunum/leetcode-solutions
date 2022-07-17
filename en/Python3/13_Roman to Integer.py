# @algorithm @lc id=13 lang=python3
# @title roman-to-integer
from en.Python3.mod.preImport import *
class Solution:
    def romanToInt(self, s: str) -> int:
        singles = dict((
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000)
        ))
        doubles = dict((
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900)
        ))
        num = 0
        while s:
            if len(s) > 1:
                if s[0:2] in doubles:
                    num += doubles[s[0:2]]
                    s = s[2:]
                else:
                    num += singles[s[0]]
                    s = s[1:]
            else:
                num += singles[s[0]]
                s = s[1:]
        return num
        