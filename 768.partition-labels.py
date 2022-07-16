
#
# @lc app=leetcode id=768 lang='python3'
#
# [768] Partition Labels
#

# @lc code=start
        
class Solution:
    # really just two steps
    # find start and end of each characters occurance index range
    # merge overlapping ranges
    def partitionLabels(self, s: str) -> list[int]:
        # space O(26)
        pos = {}
        
        # run O(n) n = len(s)
        for i, c in enumerate(s):
            # grab the range for c if exists, otherwise use
            # this index as the init value
            p = pos.get(c, (i, i))
            # update value with a new end index
            pos[c] = (p[0], i)
                
        # space O(1), 26 max
        lengths = []
        # no need to sort ranges since dict keys/values are
        # sorted by insertion order and we are inserting
        # letters by first seen index (which is what we would sort by)
        ranges = iter(pos.values())
        # init the window with the first range
        window = next(ranges)
        # run O(1), 25 max
        for start, end in ranges:
            # this range overlaps the current window, update window
            # with this ranges end if it exceeds window end
            if window[0] < start < window[1]:
                window = (window[0], max(window[1], end))
            # range doesn't overlap window, add the length of the current
            # window and start a new window with this range
            else:
                # need to add one to range difference.  if start and end
                # are the same value, we need to make sure that counts as
                # a length of 1
                lengths.append(1 + window[1] - window[0])
                window = (start, end)
        # don't forget to add the last window
        lengths.append(1 + window[1] - window[0])
        
        return lengths
# @lc code=end