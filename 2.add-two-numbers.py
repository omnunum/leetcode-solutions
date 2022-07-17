#
# @lc app=leetcode id=2 lang='python3'
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        while True:
            curr.val += l1.val + l2.val
            next_add_to, curr.val = divmod(curr.val, 10)
            if (l1.next or l2.next) is not None:
                curr.next = ListNode(next_add_to)
                curr = curr.next
                l1, l2 = l1.next or ListNode(), l2.next or ListNode()
            else:
                if next_add_to:
                    curr.next = ListNode(next_add_to)
                return head 
# @lc code=end