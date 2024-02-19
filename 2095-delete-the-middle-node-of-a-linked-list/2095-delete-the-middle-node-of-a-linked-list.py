# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        slow=head
        fast=head
        if slow.next==None:
            return None
        while fast and fast.next:
            dummy=dummy.next
            slow=slow.next
            fast=fast.next.next
        dummy.next=slow.next
        return head
        