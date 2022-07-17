# @algorithm @lc id=543 lang=python3
# @title diameter-of-binary-tree
from en.Python3.mod.preImport import *
# T = A fucking hour
class Solution:
    maxd = 0
    
    def recurse(self, node: TreeNode) -> int:
            if node is None:
                return 0
            left = self.recurse(node.left)
            right = self.recurse(node.right)
            if (m := left + right) > self.maxd:
                self.maxd = m
            return max(left, right) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = self.recurse(root)
        return self.maxd
                