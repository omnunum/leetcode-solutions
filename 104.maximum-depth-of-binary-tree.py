#
# @lc app=leetcode id=104 lang='python3'
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxd = 1
        q = [(1, root)]
        while q:
            i, n = q.pop()
            if n.left:
                q.append((i + 1, n.left))
            if n.right:
                q.append((i + 1, n.right))
            if i > maxd:
                maxd = i
        return maxd
# @lc code=end