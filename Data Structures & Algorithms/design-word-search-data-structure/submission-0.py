class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = Node()
            curr = curr.children[x]                   
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(root, idx = 0):
            curr = root
            for i in range(idx, len(word)):
                c = word[i]                
                if c == '.':
                    for x in curr.children.values():
                        if dfs(x, i+1):
                            return True
                    return False                                                                        
                else:                
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end    
        
        return dfs(curr)            
        
