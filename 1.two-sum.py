#
# @lc app=leetcode id=1 lang='python3'
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapped = dict()
        for i, n in enumerate(nums):
            mn = mapped.get(n)
            if mn is None:
                mapped[n] = (i,)
            else:
                mapped[n] = (*mapped[n], i)
            compliment = mapped.get(target - n)
            if compliment is None or (compliment[0] == i and len(compliment) == 1):
                continue
            if compliment[0] == i:
                return [i, compliment[1]]
            else:
                return [i, compliment[0]]
                
# @lc code=end