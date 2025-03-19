class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        allCourses = set()
        for a,b in prerequisites:
            allCourses.add(a)
            allCourses.add(b)
        indegree = {course:0 for course in allCourses}
        connections = collections.defaultdict(list)
        for a,b in prerequisites:
            connections[b].append(a)
            indegree[a] += 1
        q=deque()
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        visited = []
        while q:
            node = q.popleft()
            visited.append(node)
            for neighbor in connections[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return len(visited) == len(allCourses)

        