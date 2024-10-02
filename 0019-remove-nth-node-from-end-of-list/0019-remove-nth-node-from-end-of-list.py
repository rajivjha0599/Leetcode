# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            
        if not head:
            return None
        
        dummy = ListNode()
        dummy = head
        length = 0
        while dummy:
            length+=1
            dummy = dummy.next
        if(length ==1):
            return None
        if(n == length):
            return head.next
        position =  length - n
        curr = head
        pt = 1
        while pt != position:
            curr = curr.next
            pt+=1
        
        curr.next= curr.next.next

        return head