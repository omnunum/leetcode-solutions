# @algorithm @lc id=100 lang=python3
# @title same-tree
from en.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque([(p, q)])
        
        while dq:
            p, q = dq.popleft()
            if not q and not p:
                continue
            if not (q and p):
                return False
            if p.val != q.val:
                return False
            dq.append((p.left, q.left))
            dq.append((p.right, q.right))

        return True