# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0

        def reverse(node:Optional[ListNode])->ListNode:
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        otherHalf = reverse(slow)

        c1 = otherHalf
        c2 = head
        while c1:
            ans = max(ans,c1.val+c2.val) 
            c1 = c1.next
            c2 = c2.next
        return ans  