class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mappings = collections.defaultdict(list)
        for a,b in edges:
            mappings[a].append(b)
            mappings[b].append(a)
        
        visited = set()
        def traversal(node):
            if node in visited:
                return
            visited.add(node)
            for nbh in mappings[node]:
                if nbh not in visited:
                    traversal(nbh)
        counter = 0
        for i in range(n):
            if i not in visited:
                traversal(i)
                counter +=1

        return counter