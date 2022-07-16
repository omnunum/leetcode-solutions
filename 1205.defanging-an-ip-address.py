
#
# @lc app=leetcode id=1205 lang='python3'
#
# [1205] Defanging an IP Address
#

# @lc code=start
        
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
# @lc code=end