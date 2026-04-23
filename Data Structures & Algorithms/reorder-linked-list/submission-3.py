# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pref = suf = head
        while suf:
            if suf.next and not suf.next.next:
                last = suf.next
                temp = pref.next
                suf.next = None
                last.next = pref.next
                pref.next = last
                pref = suf = temp
            suf = suf.next                