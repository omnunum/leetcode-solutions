
#
# @lc app=leetcode id=883 lang='python3'
#
# [883] Car Fleet
#

# @lc code=start
        
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        stats = (
            (
                p := position[i], 
                s := speed[i], 
                (target - p) / s
            ) for i in range(n)
        )
        road = sorted(stats, key=lambda x: x[0], reverse=True)
        fleets = 1
        prev_speed = road[0][2]
        for ci in range(1, n):
            if prev_speed >= (curr_speed := road[ci][2]):
                continue
            prev_speed = curr_speed
            fleets += 1
        return fleets
# @lc code=end