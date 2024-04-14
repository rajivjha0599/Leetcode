# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddlist     = ListNode(0)
        evenlist    = ListNode(0)
        even = evenlist
        odd  = oddlist
        isodd=True
        while head:
            if isodd:
                odd.next=head
                odd = head
            else:
                even.next=head
                even = head
            head = head.next
            isodd =not isodd
        even.next=None
        odd.next=evenlist.next
        return oddlist.next
                