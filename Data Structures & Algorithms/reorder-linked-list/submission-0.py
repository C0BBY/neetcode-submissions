# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = r = head
        prev = None
        while l:
            if r.next:
                prev, r = r, r.next
            elif l.next:
                prev.next = None
                temp = l.next
                r.next = l.next
                l.next = r 
                l = r = temp              
            else:
                break