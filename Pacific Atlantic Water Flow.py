class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m = len(heights)
        n = len(heights[0])
        p = [[False] * n for _ in range(m)]
        a = [[False] * n for _ in range(m)]

        def helper(r, c, ocean_flow, prev_height):
            if r < 0 or r >= m or c < 0 or c >= n or ocean_flow[r][c] or heights[r][c] < prev_height:
                return
            ocean_flow[r][c] = True
            helper(r + 1, c, ocean_flow, heights[r][c])
            helper(r - 1, c, ocean_flow, heights[r][c])
            helper(r, c + 1, ocean_flow, heights[r][c])
            helper(r, c - 1, ocean_flow, heights[r][c])

        for r in range(m):
            helper(r, 0, p, heights[r][0])  
        for c in range(n):
            helper(0, c, p, heights[0][c]) 

        for r in range(m):
            helper(r, n - 1, a, heights[r][n - 1])  
        for c in range(n):
            helper(m - 1, c, a, heights[m - 1][c])

        result = []
        for r in range(m):
            for c in range(n):
                if p[r][c] and a[r][c]:
                    result.append([r, c])

        return result
