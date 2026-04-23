class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = Node()
            curr = curr.children[x]
        curr.end = True              
                
    def search(self, word: str) -> bool:
        curr = self.root
        for x in word:
            if x not in curr.children:
                return False
            curr = curr.children[x]
        return curr.end             


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for x in prefix:
            if x not in curr.children:
                return False
            curr = curr.children[x]                
        return True                
        