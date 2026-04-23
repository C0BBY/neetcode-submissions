class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)            
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            self.remove(self.cache.pop(self.head.key))

    def remove(self, node):
        if node is self.head:
            self.head = node.next
        elif node is self.tail:
            self.tail = node.prev            
        else:
            node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, node):                    
        if not self.head:
            self.head = self.tail = node 
            return
        node.next = None
        self.tail.next = node
        node.prev = self.tail
        self.tail=node






