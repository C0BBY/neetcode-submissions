class Node:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = None


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            node = self.head
            self.remove(node)
            self.cache.pop(node.key)
    
    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
        elif node is self.tail:
            self.tail = self.tail.prev
        else:            
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next, node.prev = node, self.tail
        self.tail = node              