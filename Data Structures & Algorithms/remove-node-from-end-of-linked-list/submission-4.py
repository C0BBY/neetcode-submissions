# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        joint = None
        curr = head

        while curr:
            if not n:
                joint = head if not joint else joint.next
            else:
                n-=1                    
            curr = curr.next

        if joint:
            joint.next = joint.next.next
        else:
            head = head.next
        return head                                