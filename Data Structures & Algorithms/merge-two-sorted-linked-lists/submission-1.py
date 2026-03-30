# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
have two tmp pointer pointing to the head of each list
    merge until reach the end of one list
add the rest of the leftover list to the tail
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp1, tmp2 = list1, list2
        dummy = ListNode(0)
        cur = dummy
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                cur.next = tmp1
                tmp1 = tmp1.next
            else:
                cur.next = tmp2
                tmp2 = tmp2.next
            cur = cur.next
        
        if tmp1:
            cur.next = tmp1
        if tmp2:
            cur.next = tmp2
        return dummy.next