"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        store = {}
        curr = head
        while curr:
            store[curr] = Node(curr.val)
            curr = curr.next
        
        for x in store.keys():
            store[x].next = store.get(x.next)
            store[x].random = store.get(x.random)
            
        return store[head]