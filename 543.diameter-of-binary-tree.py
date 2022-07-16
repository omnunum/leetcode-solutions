
#
# @lc app=leetcode id=543 lang='python3'
#
# [543] Diameter of Binary Tree
#

# @lc code=start
        
# T = A fucking hour
class Solution:
    maxd = 0
    
    def recurse(self, node) -> int:
            if node is None:
                return 0
            left = self.recurse(node.left)
            right = self.recurse(node.right)
            if (m := left + right) > self.maxd:
                self.maxd = m
            return max(left, right) + 1
        
    def diameterOfBinaryTree(self, root) -> int:
        d = self.recurse(root)
        return self.maxd
                
# @lc code=end