# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(root,target):
            if root == None:return 0
            return traverse(root.left,target) + traverse(root.right,target) + summation(root,target)
        
        def summation(root,target):
            
            if root == None:return 0
            count = 0
            if root.val == target: count = 1
            
            newtarget = target - root.val
            count   +=summation(root.left, newtarget)
            count   +=summation(root.right, newtarget)
            return count
        
        return traverse(root,targetSum)
        