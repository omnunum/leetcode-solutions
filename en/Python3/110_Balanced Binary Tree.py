# @algorithm @lc id=110 lang=python3
# @title balanced-binary-tree
from en.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, node: TreeNode) -> None:
        if not node:
            return 0
        
        left = self.recurse(node.left)
        right = self.recurse(node.right)
        
        if abs(left - right) > 1:
            raise ValueError("tree is not balanced")
            
        return max(left, right) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        try:
            self.recurse(root)
            return True
        except ValueError:
            return False
