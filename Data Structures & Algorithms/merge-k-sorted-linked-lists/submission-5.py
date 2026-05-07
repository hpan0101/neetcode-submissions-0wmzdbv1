# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        minHeap = []
        dummy = ListNode(0)
        cur = dummy

        # add all the head to the heap
        for node in lists:
            if node:
                heapq.heappush(minHeap, NodeWrapper(node))
        
        while minHeap:
            nodeWrapper = heapq.heappop(minHeap)
            cur.next = curNode = nodeWrapper.node
            cur = cur.next

            nextNode = curNode.next
            if nextNode:
                heapq.heappush(minHeap, NodeWrapper(nextNode))
        
        return dummy.next
        