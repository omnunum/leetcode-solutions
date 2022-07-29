# @algorithm @lc id=1544 lang=python3 
# @title count-good-nodes-in-binary-tree


from en.Python3.mod.preImport import *
# @test([3,1,4,3,null,1,5])=4
# @test([3,3,null,4,2])=3
# @test([1])=1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0
        q = [(root, root.val)]
        while q:
            node, max_val_on_path = q.pop()
            if max_val_on_path <= node.val:
                good_count += 1
            new_max = max(max_val_on_path, node.val)
            if node.right:
                q.append((node.right, new_max))
            if node.left:
                q.append((node.left, new_max))
        return good_count