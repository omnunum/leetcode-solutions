#
# @lc app=leetcode id=133 lang='python3'
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        root_copy = Node(node.val)
        if node.neighbors == []:
            return root_copy
        lookup = {root_copy.val: root_copy}
        q = deque([(root_copy, node)])
        while q:
            copy, node = q.pop()
            for n in node.neighbors:
                if n.val not in lookup:
                    lookup[n.val] = nc = Node(n.val)
                    q.appendleft((nc, n))
                else:
                    nc = lookup[n.val]
                copy.neighbors.append(nc)
        return root_copy
# @lc code=end