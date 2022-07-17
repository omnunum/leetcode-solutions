#
# @lc app=leetcode id=138 lang='python3'
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# T = 15min
class Solution:
    # not the most memory efficient because it needs
    # the dictionary as well as the entire stack memory
    # for each node since we're backtracking to add
    # the random attribute.
    # really really fast though
    def recurse_node(self, mapper: dict, node: 'Node', parent_copy: 'Node') -> 'Node':
        if not node:
            return
        copy = Node(node.val)
        mapper[node] = copy
        if parent_copy:
            parent_copy.next = copy
        self.recurse_node(mapper, node.next, copy)
        copy.random = mapper[node.random] if node.random is not None else None
        return copy
    
    # much slower due to more dict lookups, 
    # but also much more memory efficient as we're using 
    # the same amount of memory for the dict, but a constant
    # amount for our iterative "stack".
    def iterate_node(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        mapper, prev, node = {}, None, head
        
        while node:
            if not (curr := mapper.get(node)):
                curr = Node(node.val)
                mapper[node] = curr
                
            if prev:
                prev.next = curr
                
            random = mapper.get(node.random)
            if node.random and not random:
                    curr.random = Node(node.random.val)
                    mapper[node.random] = curr.random
            if random:
                curr.random = random
                
            prev = curr
            node = node.next
        
        return mapper[head]
    
    # very fast because the most expensive thing is looking
    # up keys in the mapper, which is avoided by just
    # adding all of the nodes to te mapper first
    # then traversing again swapping out the next and 
    # random values from the mapper.  has the best memory
    # since it uses the least amount of state
    def double_iterate_node(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        mapper, node = {}, head
        
        while node:
            mapper[node] = Node(node.val, node.next, node.random)
            node = node.next
            
        node = mapper[head]
        while node:
            if node.next:
                node.next = mapper[node.next]
            if node.random:
                node.random = mapper[node.random]
            node = node.next
        return mapper[head]
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # return self.recurse_node({}, head, None)
        # return self.iterate_node(head)
        return self.double_iterate_node(head)
        
# @lc code=end