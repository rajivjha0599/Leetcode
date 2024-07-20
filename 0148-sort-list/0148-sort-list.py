# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getmid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left  = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left,right)
    
    def getmid(self,head):
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self,L1,L2):
        t = d = ListNode()
        while L1 and L2:
            if L1.val < L2.val:
                t.next = L1
                L1 = L1.next
            else:
                t.next =L2
                L2=L2.next
            t = t.next
        if L1:
            t.next = L1
        if L2:
            t.next = L2
            
        return d.next