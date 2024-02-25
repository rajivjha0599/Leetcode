# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy2=ListNode()
        dummy.next=head
        dummy2.next=head
        if k==0:
            return head
        if head==None:
            return None
        counter=0
        while dummy.next:
            dummy=dummy.next
            counter=counter+1
        if(counter==1):
            return head
        elif(k<counter):
            numberOfRotations=counter-k
        elif (k%counter==0):
            return head
        
        else:
            DummyVar=k%counter
            numberOfRotations=counter-DummyVar

        counter=0
        while counter<numberOfRotations:
            dummy2=dummy2.next
            counter+=1
        test=dummy2.next
        dummy2.next=None
        dummy.next=head
        return test
        
        