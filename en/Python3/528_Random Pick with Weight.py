# @algorithm @lc id=912 lang=python3 
# @title random-pick-with-weight
from en.Python3.mod.preImport import *
import random
import random
from bisect import bisect_left
class Solution:
    def __init__(self, w: List[int]):
        self.cum_weights = [w[0]]
        for weight in w[1:]:
            self.cum_weights.append(self.cum_weights[-1] + weight)

    def pickIndex(self) -> int:
        rand = random.randint(1, self.cum_weights[-1])
        return bisect_left(self.cum_weights, rand)