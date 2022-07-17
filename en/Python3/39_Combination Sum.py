# @algorithm @lc id=39 lang=python3
# @title combination-sum
from en.Python3.mod.preImport import *
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        stack, combs = [], []      
        
        def dfs(i: int, target: int):
            nonlocal candidates, stack, combs
            
            if target == 0:
                combs.append(tuple(stack))
                return

            if target < 0 or i == len(candidates):
                return 

            # decision to add this number
            c = candidates[i]
            stack.append(c)
            dfs(i, target - c)

            # decision to add the next number
            stack.pop()
            dfs(i+1, target)
        
        dfs(0, target)
        return combs