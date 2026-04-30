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
        mapper = {}
        curr = head

        while curr:
            mapper[curr] = Node(curr.val)
            if curr.random and curr.random not in mapper:
                mapper[curr.random] = Node(curr.random.val)                
            curr = curr.next
                
        for curr in mapper.keys():
            mapper[curr].next = mapper.get(curr.next)
            mapper[curr].random = mapper.get(curr.random)
        
        return mapper.get(head)