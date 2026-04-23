# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = cursor = head
        prev = None
        while curr:
            if not n:
                prev = cursor
                cursor = cursor.next
            else:
                n-=1                            
            curr = curr.next                    
        if prev:
            prev.next = cursor.next
        else:
            return cursor.next                        
        return head
