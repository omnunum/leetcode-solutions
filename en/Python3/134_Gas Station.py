# @algorithm @lc id=134 lang=python3 
# @title gas-station


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5],[3,4,5,1,2])=3
# @test([2,3,4],[3,4,3])=-1
# @test([1,2,3,4,5,5,70],[2,3,4,3,9,6,2]))=6
# @test([1,2,3,4,3,2,4,1,5,3,2,4],[1,1,1,3,2,4,3,6,7,4,3,1])=-1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # diff = gas = [-2,-2,-2,3,3]
        n = len(gas)
        li, ri, total = 0, 1, gas[0] - cost[0]

        if n == 1:
            return li if total >= 0 else -1

        while ri - li < n and ri < n*2:
            ri_diff = gas[ri%n] - cost[ri%n]
            if total < 0:
                total = ri_diff
                li, ri = ri, ri + 1
            else:
                total += ri_diff
                ri += 1

        return li if ri - li == n and total >= 0 else -1
        
            
            
        