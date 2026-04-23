# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        store = []
        curr = head
        pivot = None
        prev = None
        count = 1
        while curr:
            if count >= n:
                prev, pivot = pivot, pivot.next if pivot else head
            store.append(curr)
            curr = curr.next
            if curr:
                count += 1

        if not prev:
            head = head.next
        else:
            prev.next = pivot.next
        return head
