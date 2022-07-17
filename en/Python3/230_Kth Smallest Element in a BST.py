# @algorithm @lc id=230 lang=python3
# @title kth-smallest-element-in-a-bst
from en.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr, stack = root, []
        n = 0
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            
            if n == k:
                return curr.val
            
            if curr:
                curr = curr.right