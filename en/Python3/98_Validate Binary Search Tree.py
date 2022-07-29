# @algorithm @lc id=98 lang=python3
# @title validate-binary-search-tree
from en.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# @test([2,1,3])=true
# @test([5,4,6,null,null,3,7])=false
    def isValidBST(self, root: TreeNode = None) -> bool:
        # The root node will always be valid, because it will
        # not need to be les or greater than anything.
        q = [(root, float("-inf"), float("inf"))]
        while q:
            node, min_seen, max_seen = q.pop()
            # Make sure we are still within the constraints
            if not min_seen < node.val < max_seen:
                return False
            # If we go left, then that node needs to be greater than
            # the minimum we've seen so far, and less than this node.
            # When travelling fully left biased, we will always be passing
            # along the initial min_see, which was -inf, because the fully
            # left node doesn't need to be greater than anything.
            if node.left is not None:
                q.append((node.left, min_seen, node.val))
            # Vice versa for the right side.
            if node.right is not None:
                q.append((node.right, node.val, max_seen))
        return True
            