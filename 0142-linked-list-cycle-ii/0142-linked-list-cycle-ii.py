# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data=[]
        while head:
            if head not in data:
                data.append(head)
                head=head.next
            else:
                return head
        return None
            
        