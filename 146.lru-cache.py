
#
# @lc app=leetcode id=146 lang='python3'
#
# [146] LRU Cache
#

# @lc code=start
        
# from collections import OrderedDict 
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.cap = capacity
    
#     def get(self, key: int) -> int:
#         if self.cache.get(key) is None:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
    
#     def put(self, key: int, value: int) -> None:
#         self.cache[key] = value
#         self.cache.move_to_end(key)
#         if len(self.cache) > self.cap:
#             self.cache.popitem(last=False)
#         return
    
class Node:
    def __init__(self, 
        key: str=None, 
        value: str=None, 
        next: 'Node'=None, 
        prev: 'Node'=None
    ):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
    def __repr__(self):
        return str([n.key for n in self._traverse(self)])
    
    def _traverse(self, n):
        if not n:
            return
        yield n
        yield from self._traverse(n.next)
            
class LRUCache:

    def __init__(self, capacity: int):
        self.mapper = {}
        self.cap = capacity
        self.head = Node('head')
        self.tail = Node('tail', prev=self.head)
        self.head.next = self.tail
        
    def _shift_to_tail(self, n: 'Node'):
        # test if the node already exists in the graph
        # by checking if it is tied to nodes already
        # np-><-n-><-nn ==> np-><-nn
        np, nn = n.prev, n.next
        if np is not None and nn is not None:
            np.next, nn.prev = nn, np
        # then insert node inbetween tail and its neighbor
        # tp-><-t ==> tp-><-n-><-t
        tp, t = self.tail.prev, self.tail
        tp.next, t.prev = n, n
        n.prev, n.next = tp, t
    
    def _remove_from_head(self):
        # h-><-n-><-nn ==> h-><-nn
        h, n, nn = self.head, self.head.next, self.head.next.next
        h.next, nn.prev = nn, h
        del self.mapper[n.key]
        del n
        
    def get(self, key: int) -> int:
        if (n := self.mapper.get(key)) is None:
            return -1
        self._shift_to_tail(n)
        return n.value
    
    def put(self, key: int, value: int) -> None:
        if (n := self.mapper.get(key)) is None:
            n = Node(key, value)
            self.mapper[key] = n
        n.value = value
        self._shift_to_tail(n)
        if len(self.mapper) > self.cap:
            self._remove_from_head()
        return

# @lc code=end