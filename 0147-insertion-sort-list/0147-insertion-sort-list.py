# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        
        while curr and curr.next:
            if curr.next.val >= curr.val:
                curr = curr.next
            else:
                ins = curr.next
                curr.next = ins.next
                
                pos = dummy
                
                while pos.next and pos.next.val < ins.val:
                    pos = pos.next
                
                ins.next = pos.next
                pos.next = ins
        return dummy.next
            
            