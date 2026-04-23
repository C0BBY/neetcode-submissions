# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        main = lists.pop()
        while lists:
            head = dummy = ListNode()
            curr  = lists.pop()            
            while curr and main:
                if main.val < curr.val:
                    dummy.next = ListNode(main.val)
                    main = main.next
                else:
                    dummy.next = ListNode(curr.val)
                    curr = curr.next
                dummy = dummy.next
            dummy.next = curr or main
            main = head.next
        
        return main            
            