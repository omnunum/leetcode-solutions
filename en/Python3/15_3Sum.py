# @algorithm @lc id=15 lang=python3
# @title 3sum
from en.Python3.mod.preImport import *
from collections import defaultdict
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        trips = set()
        lookup = defaultdict(set)
        nums_small = []
        for n in nums:
            if len(lookup[n]) > 2:
                continue
            nums_small.append(n)
            lookup[n].add(len(nums_small) - 1)
        size = len(nums_small)
        for li, l in enumerate(nums_small):
            for ri in range(li+1, size):
                r = nums_small[ri]
                opposite = 0 - (l + r)
                if not (ois := lookup.get(opposite)):
                    continue
                if ois - set((li, ri)):
                    trips.add(tuple(sorted((opposite, l, r))))
        return trips