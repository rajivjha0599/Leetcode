class Solution(object):

    
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            sum=(v1+v2+carry)
            digit = sum % 10
            carry = sum // 10
               
            
            curr.next = ListNode(digit)
            
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
        
        