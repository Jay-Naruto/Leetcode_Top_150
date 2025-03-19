class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def detectCycle(graph, visited, node, parent):
            visited.add(node)
            for nbh in graph[node]:
                if nbh not in visited:
                    if detectCycle(graph,visited, nbh, node):
                        return True
                elif nbh != parent:
                    return True
            return False
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        if detectCycle(graph, visited, 0, -1):
            return False
            
        return len(visited) == n

        
        