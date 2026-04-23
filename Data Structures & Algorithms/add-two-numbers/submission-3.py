# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = curr = ListNode()
        
        while l1 or l2 or carry:
            count = carry
            if l1:
                count += l1.val
                l1 = l1.next
            if l2:
                count += l2.val
                l2 = l2.next
            
            val = count%10
            carry = count//10
            curr.next = ListNode(val)
            curr = curr.next
        
        return head.next

