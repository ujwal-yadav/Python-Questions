# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst=[]
        itr=head
        if itr is None:
            return False
        else:
            while itr:
                if itr.next is None:
                    return False
                if id(itr) not in lst:
                    lst.append(id(itr))
                else:
                    return True
                itr=itr.next
