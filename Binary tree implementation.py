class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inputTree():
    root=int(input("Enter Data: "))
    if root == -1:
        return None
    
    root=Node(root)
    
    root.left=inputTree()
    root.right=inputTree()
    
    return root
    
def printTree(root):
    if not root:
        return
    
    print("Root Node --> ",root.data,end=" ")
    if root.left:
        print("Left Child:",root.left.data,end=", ")
        
    if root.right:
        print("Right Child:",root.right.data,end="")
    
    print()
    printTree(root.left)
    printTree(root.right)

res=inputTree()
printTree(res)
