# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [[] for _ in range(k)]
        curr = head

        count = 0
        while curr:
            count+=1
            curr =  curr.next
        
        length = count//k
        remainder = count%k

        prev = None
       
        for i in range(k):
            ans[i] = head
            for j in range(length +(1 if remainder >0 else 0)):
                prev = head
                head = head.next
            if prev:
                prev.next = None
            remainder-=1
        return ans
