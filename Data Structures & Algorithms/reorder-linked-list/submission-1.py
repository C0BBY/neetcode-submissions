# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pref = suff = head

        while suff:
            if suff.next and not suff.next.next:
                last = suff.next
                suff.next = None
                last.next = pref.next
                pref.next = last
                pref = suff = last.next
                continue
            suff = suff.next