# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        def helper(prev, curr):
            if not curr or not curr.next:
                return
            next_pair = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = next_pair
            helper(curr, next_pair)

        helper(prev, head)
        return dummy.next