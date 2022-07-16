
#
# @lc app=leetcode id=199 lang='python3'
#
# [199] Binary Tree Right Side View
#

# @lc code=start
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#T = 23min
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        q = deque([(root, 0)])
        right_nodes = []
        pn, pl = root, 0
        while q:
            n, l = q.pop()
            if l > pl:
                right_nodes.append(pn.val)
            pn, pl = n, l
            if n.left:
                q.appendleft((n.left, l+1))
            if n.right:
                q.appendleft((n.right, l+1))
        right_nodes.append(n.val)
        return right_nodes
        

            
# @lc code=end