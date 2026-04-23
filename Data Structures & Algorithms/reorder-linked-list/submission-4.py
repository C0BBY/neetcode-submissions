# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = pivot = head
        while curr:
            if curr.next and not curr.next.next:
                temp = pivot.next
                last = curr.next
                last.next = pivot.next
                pivot.next = last
                curr.next = None
                curr = pivot =  temp
            curr = curr.next                