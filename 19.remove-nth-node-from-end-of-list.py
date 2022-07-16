
#
# @lc app=leetcode id=19 lang='python3'
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = deque()
        node = head
        i = 0
        while node:
            q.append((i, node))
            if (nn := node.next):
                i += 1
            node = nn
        end = i
        axed_next = None
        while q:
            i, node = q.pop()
            if i == end + 1 - n:
                axed_next = node.next
                break
        if q:
            i, prev = q.pop()
            prev.next = axed_next
            return head
        return axed_next
            
# @lc code=end