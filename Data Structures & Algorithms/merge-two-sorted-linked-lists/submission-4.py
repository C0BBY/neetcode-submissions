# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        
        def merge(ls1, ls2, tail):
            if not ls1 or not ls2:
                tail.next = ls1 or ls2
                return

            if ls1.val < ls2.val:
                tail.next, ls1 = ls1, ls1.next
            else:              
                tail.next, ls2 = ls2, ls2.next 

            merge(ls1, ls2, tail.next)

        merge(list1, list2, tail)
        return dummy.next