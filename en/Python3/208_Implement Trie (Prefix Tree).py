# @algorithm @lc id=208 lang=python3
# @title implement-trie-prefix-tree
from en.Python3.mod.preImport import *
from collections import deque
class Trie:

    def __init__(self):
        self.start = {}

    def insert(self, word: str) -> None:
        node = self.start
        last = len(word) - 1
        
        for i, c in enumerate(word):
            _, node = self._next_node(node, c, i == last)   
          

    def _search(self, word: str) -> bool:
        node = self.start
        last = len(word) - 1
        for i, c in enumerate(word):
            ending, node = node[c]
        return ending

    
    def search(self, word: str) -> bool:
        try:
            return self._search(word)
        except KeyError:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        try:
            _ = self._search(prefix)
            return True
        except KeyError:
            return False
    
    def _next_node(self, node, character: str, ending: bool) -> None:
        if character not in node:
            node[character] = (ending, {})
        _ending, _node = node[character]
        # if we need to add a word ending here
        if not _ending and ending:
            node[character] = (ending, _node)
        return _ending or ending, _node
        
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)