# @algorithm @lc id=43 lang=python3
# @title multiply-strings
from en.Python3.mod.preImport import *
class Solution:
    '''
    # backwards with carry
        11
    -------
        123
    *   456
    _______
        738
       615 -> * 10 * 1 = 6150
      492  -> * 10 * 2 = 49200
     
     # forwards with per loop 10xing
     0 * 10 = 0
     1 * 6 = 6 -> 60
     2 * 6 = 12 -> 72 -> 720
     3 * 6 = 18 -> 738 -> 738
     
 
     
    '''  
#     # backwards with carry
#     def multiply(self, num1: str, num2: str) -> str:
#         total = 0
#         for i, n1 in enumerate(num1[::-1]):
#             partial = 0
#             overflow = 0
#             for j, n2 in enumerate(num2[::-1]):
#                 next_overflow, remainder = divmod(int(n1) * int(n2), 10)
#                 partial += (remainder + overflow) * (10 ** j)
#                 overflow = next_overflow
#             partial += overflow * (10 ** (j+1))
#             partial *= 10 ** i
#             total += partial
            
#         return str(total)

   
    # backwards with 10xing
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        for i, n1 in enumerate(num1[::-1]):
            partial = 0
            for j, n2 in enumerate(num2[::-1]):
                partial += int(n1) * int(n2) * (10 ** j)
            partial *= 10 ** i
            total += partial
            
        return str(total)

#     # forwards with per loop 10xing
#     def multiply(self, num1: str, num2: str) -> str:
#         total = 0
#         for n1 in num1:
#             partial = 0
#             total *= 10
#             for n2 in num2:
#                 partial *= 10
#                 partial += int(n1) * int(n2)
#             total += partial
            
#         return str(total)
