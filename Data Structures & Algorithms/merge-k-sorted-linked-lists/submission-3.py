class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, NodeWrapper(node))
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            curNode = heapq.heappop(heap).node
            if curNode.next:
                heapq.heappush(heap, NodeWrapper(curNode.next))
            curr.next = curNode
            curr = curr.next
        
        return dummy.next