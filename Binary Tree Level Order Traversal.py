class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res=[]
        queue=[]
        queue.append(root)
 
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                res.append(level)
                
        return res
