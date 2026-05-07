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
        minHeap = []
        # add all the head to the heap
        for node in lists:
            if node:
                heapq.heappush(minHeap, NodeWrapper(node))
        
        dummy = ListNode(0)
        cur = dummy
        while minHeap:
            nodeWrapper = heapq.heappop(minHeap)
            curNode = nodeWrapper.node
            nextNode = curNode.next
            cur.next = curNode
            cur = cur.next
            if nextNode:
                heapq.heappush(minHeap, NodeWrapper(nextNode))
        
        return dummy.next