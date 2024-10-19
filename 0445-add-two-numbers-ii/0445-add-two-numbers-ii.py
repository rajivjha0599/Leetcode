# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        c1 = l1
        c2 = l2
        
        prev1 = None
        prev2 = None
        
        while c1:         
            temp = c1.next 
            c1.next = prev1
            prev1 = c1
            c1 =  temp       
        while c2:
            temp = c2.next 
            c2.next = prev2
            prev2 = c2
            c2 =  temp

        ans     = ListNode(0,None)
        head    = ListNode(None,ans)
        
        while prev1 or prev2:
            s1 =  prev1.val if prev1 else 0
            s2 =  prev2.val if prev2 else 0
            s3 =  ans.val if ans.val else 0
            
            temp = s1 + s2 + s3
                        
            sum = temp %10
            carry = 0 if temp < 10 else floor(temp/10)
            
            ans.val = sum            
            ans.next = ListNode(carry,None)
            prev1 = prev1.next if prev1 and prev1.next else None
            prev2 = prev2.next if prev2 and prev2.next else None
            ans = ans.next 
        if carry!= 0 and carry !=None:
            ans.next = ListNode(carry,None)
        prev = None
        c1 =  head.next 
        
        while c1:    
            temp = c1.next 
            c1.next = prev
            prev = c1
            c1 =  temp   

        return prev.next
            
            
    
    
        