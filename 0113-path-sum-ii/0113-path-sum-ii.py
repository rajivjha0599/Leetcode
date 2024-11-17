# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def helper(stack :list,root,target,total):
            if not root:
                
                return 
            total += root.val
            stack.append(root.val)
            if (not root.left and not root.right) and total == target:
                ans.append(list(stack))
  
            helper(stack,root.left,target,total)     
            helper(stack,root.right,target,total)
            stack.pop()
        helper([],root,targetSum,0)
        return ans        
            
                