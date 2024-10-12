# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less    = ListNode(0,None)
        greater = ListNode(0,None)
        
        lessHead    = less
        greaterHead = greater
        
        while head:
            if head.val < x:
                lessHead.next = head
                lessHead =  lessHead.next
            else:
                greaterHead.next = head
                greaterHead =  greaterHead.next
            
            head =  head.next
        
        greaterHead.next = None
        
        lessHead.next = greater.next
        
        return less.next