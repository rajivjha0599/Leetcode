# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev  = dummy

        while head :
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                if head.val == dummy.next.val:
                    dummy.next = head.next
                    prev = dummy
                else:
                    prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next