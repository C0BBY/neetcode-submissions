# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = deque() 
        stk2 = deque()
        while l1 or l2:
            if l1:
                stk1.append(l1.val)
                l1 = l1.next
            if l2:
                stk2.append(l2.val)
                l2 = l2.next

        print(f"l1 {len(stk1)} l2 {len(stk2)} ")
        head = curr = ListNode()
        carry = 0
        while stk1 or stk2 or carry:
            aggr = carry
            aggr+= stk1.popleft() if stk1 else 0
            aggr+= stk2.popleft() if stk2 else 0
            val = aggr%10
            carry = aggr//10
            curr.next = ListNode(val)
            curr = curr.next
            # print(f"aggr::{aggr} val::{val} carry::{carry}")

        return head.next           
