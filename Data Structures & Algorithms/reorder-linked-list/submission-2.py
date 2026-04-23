# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        container = []


        while curr:
            container.append(curr)
            curr = curr.next
        l, r = 0, len(container)-1
        
        while l < r:
            container[r].next = container[l].next
            container[l].next = container[r]
            l+=1
            r-=1            

        container[max(l,r)].next = None 