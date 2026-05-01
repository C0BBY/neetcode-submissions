class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.container = {}
        self.capacity = capacity        
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key in self.container:
            node = self.container[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.container:
            self.remove(self.container[key])                        
        self.container[key] = Node(key, value)                             
        self.insert(self.container[key])
        
        while len(self.container) > self.capacity:
            self.container.pop(self.head.key)
            self.remove(self.head)
        
    
    def insert(self, node):
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next, node.prev, node.next = node, self.tail, None 
        self.tail = node

    def remove(self, node):        
        if node is self.head:
            self.head = self.head.next
            return
        if node is self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next, node.next.prev = node.next, node.prev


