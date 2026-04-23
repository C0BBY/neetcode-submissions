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
        dummy = curr = Node(0)
        while head:
            curr.val = head.val
            if head.next:
                curr.next = Node(0)
            store[head] = curr
            curr = curr.next
            head = head.next
        
        for x in store.keys():
            if x.random:
                store[x].random = store[x.random]
        return dummy