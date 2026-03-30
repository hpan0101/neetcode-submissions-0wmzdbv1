# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
move to nth node
maintain a a pointer to head, nthpointer
keep moving by one until nthpointer.next is none
maintain prev of that node,
prev.next = node.next
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        np = head
        for i in range(n):
            if not np:
                return None
            np = np.next
        
        tmp = head
        prev = None
        while np:
            np = np.next
            prev = tmp
            tmp = tmp.next
        
        if not prev:
            return head.next
        prev.next = tmp.next
        return head
