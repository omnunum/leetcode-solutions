
#
# @lc app=leetcode id=1194 lang='python3'
#
# [1194] Path In Zigzag Labelled Binary Tree
#

# @lc code=start
        
class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        listed = []
        binary = f"{label:>64b}"
        levels = 64 - binary.index("1")
        dist_from_left = None
        this_label = label
        odd = not levels % 2
        
        for level in range(levels, 0, -1):
            max_label = (2 ** level) - 1
            min_label = 2 ** (level - 1)
            odd = not odd
            
            if dist_from_left is None:
                dist_from_left = (
                    max_label - this_label 
                    if odd
                    else this_label - min_label
                )
            else:
                dist_from_left = dist_from_left >> 1

            this_label = (
                max_label - dist_from_left 
                if odd
                else dist_from_left + min_label
            )

            listed.insert(0, this_label)
                        
        return listed
# @lc code=end