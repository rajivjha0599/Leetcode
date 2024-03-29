class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # if not list1 or not list2:
    #   return list1 if list1 else list2
    # if list1.val > list2.val:
    #   list1, list2 = list2, list1
    # list1.next = self.mergeTwoLists(list1.next, list2)
    # return list1
    dummy=ListNode()
    tail=dummy
    while list1 and list2:
        if list1.val<list2.val:
            tail.next=list1
            list1=list1.next
        else:
            tail.next=list2
            list2=list2.next
        tail=tail.next
    if list2:
        tail.next=list2
    if list1:
        tail.next=list1
    return dummy.next