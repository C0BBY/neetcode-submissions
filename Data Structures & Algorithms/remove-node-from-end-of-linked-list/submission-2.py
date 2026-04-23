# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        pivot = None
        prev = None
        count = 1
        while curr:
            if count > n:
                pivot = pivot.next if pivot else head
            curr = curr.next
            count += 1

        if not pivot:
            head = head.next
        else:
            pivot.next = pivot.next.next
        return head
