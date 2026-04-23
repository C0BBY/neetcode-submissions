class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = None        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            self.remove(self.cache.pop(self.head.key))
            

    def remove(self, node):
        if node is self.head:
            self.head = node.next
        elif node is self.tail:
            self.tail = node.prev
        else:                        
            prev, next = node.prev, node.next
            prev.next, next.prev = next, prev

    def insert(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node            