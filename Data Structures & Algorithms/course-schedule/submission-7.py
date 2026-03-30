class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegree = [0] * numCourses
        finished = 0
        for crs, prereq in prerequisites:
            adjList[prereq].append(crs)
            indegree[crs] += 1
        q = deque()
        for crs in range(len(indegree)):
            if indegree[crs] == 0:
                q.append(crs)
        
        while q:
            crs = q.popleft()
            finished += 1

            for dependent in adjList[crs]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        
        return numCourses == finished

                


'''
indegree
adj list

iterate through indegree, push the class that has zero prereq to the queue

while queue is not empty
    poll queue to get a node, reduce the indegree for the crs that has node as prereq,
    if its indegree is 0,put crs to the queue


'''