class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.revListHead=None
        
    def add(self,val):
        self.revListHead=Node(val,self.revListHead)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        while itr:
            self.add(itr.val)
            itr=itr.next
        
        return self.revListHead
