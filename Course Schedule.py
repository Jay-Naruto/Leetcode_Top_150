class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict1=collections.defaultdict(list)
        indegree = {i: 0 for i in range(numCourses)}
        for u,v in prerequisites:
            dict1[v].append(u)
            indegree[u] += 1
            
        q=deque([])
        for num in indegree:
            if indegree[num] == 0:
                q.append(num)
        visited=0
        while q:
            node = q.popleft()
            visited += 1
            for neighbor in dict1[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return numCourses == visited
        