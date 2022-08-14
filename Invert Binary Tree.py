Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invert(self,root):
        if not root:
            return
        nr=TreeNode(root.val)
        nr.left=self.invert(root.right)
        nr.right=self.invert(root.left)
        return nr
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res=self.invert(root)
        return res
