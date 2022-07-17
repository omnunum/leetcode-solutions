#
# @lc app=leetcode id=98 lang='python3'
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node: TreeNode) -> (int|float, int|float):
        if not node:
            return float("inf"), float("-inf")
        
        left_min, left_max = self.traverse(node.left)
        right_min, right_max = self.traverse(node.right)
        
        if left_max >= node.val:
            raise ValueError(f"node {node.val} has a node in its left subtree of {left_max}, which is greater than or equal to its val")
        if right_min <= node.val:
            raise ValueError(f"node {node.val} has a value in its right subtree of {left_max}, which is less than or equal to its val")
        
        return min(left_min, right_min, node.val), max(left_max, right_max, node.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        try:
            self.traverse(root)
            return True
        except ValueError:
            return False
            
# @lc code=end