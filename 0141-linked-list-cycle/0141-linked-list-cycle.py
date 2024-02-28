# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        data=[]
        while head:
            if head not in data:
                data.append(head)
                head=head.next
            else:
                return True
        return False
        