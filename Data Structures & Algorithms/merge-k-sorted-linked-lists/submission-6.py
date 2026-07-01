# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0)
        cur = dummy
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))
        
        while heap:
            curHeapNode = heapq.heappop(heap)
            curNode = curHeapNode.node
            cur.next = curNode
            cur = cur.next
            if curNode.next:
                heapq.heappush(heap, HeapNode(curNode.next))
        
        return dummy.next