# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        values = []
        stack = []
        while head:
            values.append(head.val)
            head = head.next
        ans = [0]*len(values)
        
        for i,value in enumerate(values):
            while stack and values[stack[-1]] < value:
                index = stack.pop()
                ans[index] = value
            stack.append(i)
        return ans