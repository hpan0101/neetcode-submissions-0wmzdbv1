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
        dummy = ListNode(0, head)
        right = head
        left = dummy

        for i in range(n):
            if not right:
                return None
            right = right.next
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next
