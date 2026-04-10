# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    bfs
        add root to queue
        while queue is not empty:
            for each level, 
            pop all the elemets in the queue, 
            store to result list, 
            add their kids to the queue
        return res
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            curLevel = []
            for _ in range(size):
                curNode = q.popleft()
                curLevel.append(curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            res.append(curLevel)
        return res

        