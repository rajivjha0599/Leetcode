# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root: return
        def dfs(node,tracker):
            nonlocal ans
            if not node:return
            if tracker == 'left' and node.left == None and node.right== None:
                ans += node.val
                
            dfs(node.left,"left")
            dfs(node.right,"right")
        dfs(root,"root")
        return ans