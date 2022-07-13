class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
    
class MyLinkedList:

    def __init__(self):
        self.head=None
        
    def listSize(self):
        itr=self.head
        c=0
        while itr:
            c+=1
            itr=itr.next
        return c
            
    def get(self, index: int) -> int:
        if index < 0 or index >= self.listSize():
            return -1
        
        if self.head is None:
            return -1
        
        itr=self.head
        c=0
        
        while itr:
            if c==index:
                return itr.val
            c+=1
            itr=itr.next
        
        
    def addAtHead(self, val: int) -> None:
        self.head=Node(val,self.head)

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head=Node(val,None)
            return 
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(val,None)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        
        itr=self.head
        c=0
        while itr:
            if c==index-1:
                itr.next=Node(val,itr.next)
                break
            itr=itr.next
            c+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.listSize():
            return
        if index==0:
            self.head=self.head.next
            return
        
        itr=self.head
        c=0
        while itr:
            if c==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            c+=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
