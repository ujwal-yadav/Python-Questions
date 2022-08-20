class Solution:
    prev=None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            if not self.isValidBST(root.left):
                return False
            
            if self.prev is not None and self.prev.val>=root.val:
                return False
            
            self.prev=root
            
            return self.isValidBST(root.right)
            
        return True
