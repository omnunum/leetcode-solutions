# @algorithm @lc id=211 lang=python3
# @title design-add-and-search-words-data-structure
from en.Python3.mod.preImport import *
class WordDictionary:

    def __init__(self):
        self.store = {}

    def addWord(self, word: str) -> None:
        prev = self.store.get(word[0], {})
        self.store[word[0]] = prev
        for c in word[1:]:
            if not (curr := prev.get(c, {})):
                prev[c] = curr
            prev = curr
        prev["*"] = {}
    
    def _recurse(self, node: dict, chars: str) -> bool:
        if not chars and "*" in node:
            return True
        elif not chars:
            return False
        c = chars[0]
        if c == '.':
            for nc in node:
                if self._recurse(node[nc], chars[1:]):
                    return True
            return False
        elif c in node:
            return self._recurse(node[c], chars[1:])
        return False
        
        
    def search(self, word: str) -> bool:
        return self._recurse(self.store, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)