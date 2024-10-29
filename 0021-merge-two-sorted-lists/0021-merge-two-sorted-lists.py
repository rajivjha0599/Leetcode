class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummy=ListNode()
    tail=dummy

    def helper(list1,list2,tail):
        if not list1:
            tail.next = list2
            return dummy.next
        if not list2:
            tail.next = list1
            return dummy.next
        
        if list1.val<list2.val:
            tail.next = list1
            return helper(list1.next,list2,tail.next)
        
        else:
            tail.next = list2
            return helper(list1,list2.next,tail.next)
    return helper(list1,list2,tail)

    