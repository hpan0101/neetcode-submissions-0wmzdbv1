# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
find mid using slow and fast
reverse the last half(slow.next)
merge the two lists
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next: return

        slow = self.findMid(head)
        mid = slow.next
        slow.next = None

        newLastHalfHead = self.reverse(mid)

        newHead = self.mergeLists(head, newLastHalfHead)
    
    def mergeLists(self, l1: Optiona[ListNode], l2: Optiona[ListNode]) -> Optiona[ListNode]:
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            if tmp1 is None:
                break
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2

    def reverse(self, head: Optiona[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
    
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    