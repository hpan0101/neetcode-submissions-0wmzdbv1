class Solution:
    '''
    add course, prereq to adjlist
    add indegree[pre] += 1
    [0, 1],[1, 2]
         0  1   2
    adj[[],[0],[1]]
    indegree = {1, 1, 0}

    ''' 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        indegree= [0] * numCourses
        order = []

        for crs, preq in prerequisites:
            adjList[preq].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
            
        while q:
            crs = q.popleft()
            order.append(crs)
            for dependent in adjList[crs]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        
        return order if len(order) == numCourses else []