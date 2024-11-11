# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next
        
        newHead = self.reverse(head,tail)
        head.next = self.reverseKGroup(tail, k)
        return newHead

        
    def reverse(self,head,tail):
        prev = None
        curr =  head
        while curr != tail:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        return prev
    
            
        
        
        
        
        
            