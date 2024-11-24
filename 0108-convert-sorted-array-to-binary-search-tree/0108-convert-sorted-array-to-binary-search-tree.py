# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l,r):
            if l>r:
                return 
            
            node = TreeNode(nums[(l+r)//2])
            
            node.left = helper(l,((l+r)//2)-1)
            node.right = helper(((l+r)//2)+1,r)
            
            return node
        
        return helper(0,len(nums)-1)