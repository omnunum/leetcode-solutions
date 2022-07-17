# @algorithm @lc id=341 lang=python3
# @title flatten-nested-list-iterator
from en.Python3.mod.preImport import *
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):        
        def flatten(nest) -> int:
            for n in nest:
                if n.isInteger():
                    yield n.getInteger()
                    continue
                yield from flatten(n.getList())
                
        self.gen = flatten(nestedList)
        
    def next(self) -> int:
        return self.next_val
    
    def hasNext(self) -> bool:
        self.next_val = next(self.gen, None)
        return self.next_val is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
    