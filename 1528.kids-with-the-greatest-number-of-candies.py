
#
# @lc app=leetcode id=1528 lang='python3'
#
# [1528] Kids With the Greatest Number of Candies
#

# @lc code=start
        
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        most = max(candies)
        return [(extraCandies >= most - c) for c in candies]
                   
# @lc code=end