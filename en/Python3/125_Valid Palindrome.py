# @algorithm @lc id=125 lang=python3
# @title valid-palindrome
from en.Python3.mod.preImport import *
class Solution:
    def isPalindrome(self, s: str) -> bool:
        li, ri = 0, len(s) - 1
        while ri > li:
            if not (l := s[li]).isalnum():
                li += 1
                continue
            if not (r := s[ri]).isalnum():
                ri -= 1
                continue
            if l.lower() != r.lower():
                return False
            li += 1
            ri -= 1
        return True