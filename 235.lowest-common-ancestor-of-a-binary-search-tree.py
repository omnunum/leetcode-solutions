
#
# @lc app=leetcode id=235 lang='python3'
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# T = 15
class Solution:
    def dfs(self, n, p, q):
        if not n:
            return
        if n == p:
            return p
        if n == q:
            return q
        l, r = self.dfs(n.left, p, q), self.dfs(n.right, p, q)
        if l and r:
            return n
        return l if l else r
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
        
# @lc code=end