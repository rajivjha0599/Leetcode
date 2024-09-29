# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        prev = None
        curr = head
        while curr:
            next_node = curr.next  
            curr.next = prev      
            prev = curr            
            curr = next_node       
        ct = 0
        ans = 0
        while prev:
            
            ans+=(2**(ct))*prev.val
            prev=prev.next
            ct+=1
        return ans