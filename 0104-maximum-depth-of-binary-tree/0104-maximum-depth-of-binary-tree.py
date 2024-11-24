# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        def helper(root,ans):
            nonlocal height
            if not root:
                return 
            ans+=1
            if root.left == None and root.right == None:
                height = max(ans,height)
            
            helper(root.left,ans)
            helper(root.right,ans)
        helper(root,0)
        return height