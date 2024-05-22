# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def in_order_traversal(node: TreeNode):
            if not node:
                return True
            
            if not in_order_traversal(node.left):
                return False
            
            if self.prev is not None and node.val <= self.prev:
                return False
            
            self.prev = node.val
            
            return in_order_traversal(node.right)
        
        self.prev = None
        return in_order_traversal(root)
       
        
        