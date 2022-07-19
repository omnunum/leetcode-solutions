# @algorithm @lc id=876 lang=python3 
# @title hand-of-straights
# t 17:51

from en.Python3.mod.preImport import *
# @test([1,2,3,6,2,3,4,7,8],3)=true
# @test([1,2,3,4,5],4)=false
# @test([8,10,12], 3)=false
# @test([3,4,7,4,6,3,6,5,2,8], 2)=false
# @test([1,1,2,2,3,3], 2)=false
# @test([1,1,2,2,3,3], 3)=true
from collections import Counter, deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        keys = deque(sorted(counts.keys()))
        ri, key, size = 0, keys[0], 0
        while keys:
            # if we've hit the window size limit then reset the window
            if size == groupSize:
                ri, key, size = 0, keys[0], 0
            # if we didn't hit the limit but we've exhausted all keys
            # then we know we would have needed to "repeat" keys and
            # thus aren't consecutive
            elif ri == len(keys):
                return False

            # if the difference of "this" key and the previous key
            if keys[ri] - key > 1:
                return False

            key = keys[ri]
            counts[key] -= 1

            # if we've run out of count for this number
            if counts[key] == 0:
                # but we're not at the beginning of the window
                if ri != 0:
                    # we know we'll have a gap next run broken consecutiveness
                    return False
                else:
                    keys.popleft()
                    ri = min(len(keys)-1, ri)
                    size += 1
            else:
                ri += 1
                size += 1

        return True


