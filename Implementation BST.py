class bst:
	def __init__(self, data):
	    self.data = data
	    self.left = None
	    self.right = None
        
def insert(root,ele):
    if root is None:
        return bst(ele)
    else:
        if root.data == ele:
            return root
        elif ele<root.data:
            root.left=insert(root.left,ele)
        else:
            root.right=insert(root.right,ele)
            
    return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
    
r=bst(3)
r=insert(r,2)
r=insert(r,4)
inorder(r)
