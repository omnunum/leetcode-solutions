
#
# @lc app=leetcode id=143 lang='python3'
#
# [143] Reorder List
#

# @lc code=start
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        node = head
        while node:
            q.append(node)
            node = node.next
        right = True
        oc = c = q.popleft()
        while q:
            if right:
                c.next = q.pop()
            else:
                c.next = q.popleft()
            right = not right
            c = c.next
        c.next = None
        return oc
                
# @lc code=end