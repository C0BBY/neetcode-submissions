# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        container = []
        main = dummy = ListNode()

        while head:
            container.append(head)
            if len(container) == k:
                while container:                    
                    dummy.next = ListNode(container.pop().val)
                    dummy = dummy.next                                                 
            head = head.next
        
        if container:
            dummy.next = container[0]
        
        return main.next            
