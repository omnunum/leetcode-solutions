#
# @lc app=leetcode id=21 lang='python3'
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
LN = ListNode
class Solution:
    def get_min_shifted(self, l1: LN, l2: LN):
        if l1.val <= l2.val:
            min_node = l1
            l1 = l1.next
        else:
            min_node = l2
            l2 = l2.next
        return l1, l2, min_node
    
    def recurse_sort(self, l1: LN, l2: LN, curr: LN) -> LN:
        # exit condition
        if l1 is None:
            curr.next = l2
            return
        elif l2 is None:
            curr.next = l1
            return
        
        # sort condition
        l1, l2, min_node = self.get_min_shifted(l1, l2)
            
        # recurse condition
        curr.next = min_node
        self.recurse_sort(l1, l2, curr.next)
            
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        l1, l2, root = self.get_min_shifted(l1, l2)
        
        self.recurse_sort(l1, l2, root)
        return root
        
        
# @lc code=end