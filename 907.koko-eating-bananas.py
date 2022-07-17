#
# @lc app=leetcode id=907 lang='python3'
#
# [907] Koko Eating Bananas
#

# @lc code=start
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        min_step, max_step = 1, piles[-1]
        if len(piles) == 1:
            return ceil(piles[0] / h)
        while min_step < max_step:
            if max_step - min_step > 1:
                step_size = (min_step + max_step) // 2
            else:
                return max_step
            steps = sum((ceil(p/step_size) for p in piles))
            if steps <= h:
                max_step = step_size
            elif steps > h:
                min_step = step_size
        return step_size
        
# @lc code=end