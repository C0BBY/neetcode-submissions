# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            aggr = carry
            if l1:
                aggr+= l1.val
                l1 = l1.next
            if l2:
                aggr+= l2.val
                l2 = l2.next

            val = aggr%10
            carry = aggr//10
            curr.next = ListNode(val)
            curr = curr.next
        return head.next           
