
#
# @lc app=leetcode id=66 lang='python3'
#
# [66] Plus One
#

# @lc code=start
        
class Solution:
    # # conversion therapy
    # def plusOne(self, digits: list[int]) -> list[int]:
    #     stringed = "".join([str(d) for d in digits])
    #     inted = int(stringed) + 1
    #     relisted = list(str(inted))
    #     return relisted
    
#    # legit way
#     def plusOne(self, digits: list[int]) -> list[int]:
#         overflow = 1
#         for i in range(len(digits)-1, -1, -1):
#             overflow = digits[i] + overflow
#             overflow, added = divmod(overflow, 10)
#             digits[i] = added
            
#         if overflow:
#             digits.insert(0, overflow)
            
#         return digits

    # legit way with early exit optimization
    def plusOne(self, digits: list[int]) -> list[int]:
        overflow = 1
        i = len(digits)-1
        while overflow and i >= 0:
            overflow = digits[i] + overflow
            overflow, added = divmod(overflow, 10)
            digits[i] = added
            i -= 1
            
        if overflow:
            digits.insert(0, overflow)
            
        return digits
# @lc code=end