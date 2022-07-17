#
# @lc app=leetcode id=1544 lang='python3'
#
# [1544] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# T = 5 min
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        num_good = 0
        while q:
            n, vmax = q.pop()
            if n.val >= vmax:
                num_good += 1
                vmax = n.val
            if n.left:
                q.append((n.left, vmax))
            if n.right:
                q.append((n.right, vmax))
        return num_good
# @lc code=end