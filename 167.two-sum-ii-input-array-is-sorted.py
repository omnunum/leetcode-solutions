
#
# @lc app=leetcode id=167 lang='python3'
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
        

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ns = numbers
        li, ri = 0, len(numbers) - 1
        while (summed := ns[li] + ns[ri]) != target:
            if summed > target:
                ri -= 1
                continue
            if summed < target:
                li += 1
                continue
            
        return [li + 1, ri + 1]
# @lc code=end