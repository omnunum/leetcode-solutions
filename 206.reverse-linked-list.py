#
# @lc app=leetcode id=206 lang='python3'
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# a -> b -> c -> d -> e -> None
# prev a , new b , curr c -> d -> e -> None
# new b -> prev a, curr c -> d -> e -> None
# prev = new; new = curr; curr = curr.next
# c -> b, d -> e -> None
# d -> c, e -> None
# e -> d, None
# new_head -> b, prev_head = a, curr_head = c
# 
# 1  2  3 4 5 
# 2  1  3 4 5
# 3  2  1 4 5
# 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            nx = node.next
            node.next = prev
            prev, node = node, nx
        return prev
        
        
        
# @lc code=end