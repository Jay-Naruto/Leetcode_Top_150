class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict1=collections.defaultdict(list)
        inorder={i: 0 for i in range(numCourses)}

        for u,v in prerequisites:
            dict1[v].append(u)
            inorder[u] += 1
        
        q=deque([])
        visited=[]
        for x in inorder:
            if inorder[x] == 0:
                q.append(x)
        
        while q:
            node=q.popleft()
            visited.append(node)
            for neighs in dict1[node]:
                inorder[neighs] -= 1
                if inorder[neighs] == 0:
                    q.append(neighs)

        return visited if numCourses == len(visited) else []
        