#
# @lc app=leetcode id=102 lang='python3'
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels = []
        if root is None:
            return levels
        q = deque([(root, 0)])
        while q:
            n, l = q.pop()
            if l == len(levels):
                levels.append([])
            levels[l].append(n.val)
            if n.left is not None:
                q.appendleft((n.left, l + 1))
            if n.right is not None:
                q.appendleft((n.right, l + 1))
        return levels
# @lc code=end