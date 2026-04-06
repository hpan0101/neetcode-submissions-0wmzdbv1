class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.ended = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.ended = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.ended

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True
        
        