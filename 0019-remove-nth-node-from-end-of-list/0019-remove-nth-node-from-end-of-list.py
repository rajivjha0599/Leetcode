# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=ListNode(None,head)
        counter1=0
        dummy1=head
        dummy2=head
        prev.next=dummy1
        while dummy1:
            counter1+=1
            dummy1=dummy1.next
            prev=prev.next
        counter2=0
        if counter1==1 and n==1:
            head=None
            return head
        if counter1-n==0:
            head=head.next
            return head
        while counter2<counter1-n-1:
            dummy2=dummy2.next
            counter2+=1
       
        dummy2.next=dummy2.next.next
        return head