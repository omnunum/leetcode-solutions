# @algorithm @lc id=572 lang=python3
# @title subtree-of-another-tree
from en.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# T = 15
from collections import deque
class Solution:
    def search(self, node: TreeNode, subRoot: TreeNode):
        q = deque([node])
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if self.evaluate(node, subRoot):
                    return True
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        return False
        
    def evaluate(self, node: TreeNode, sub: TreeNode):
        q = deque([(node, sub)])
        while q:
            node, sub = q.popleft()
            if not (node and sub):
                return False
            if node.val != sub.val:
                return False
            if node.left or sub.left:
                q.appendleft((node.left, sub.left))
            if node.right or sub.right:
                q.appendleft((node.right, sub.right))
        return True
                
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.search(root, subRoot)
