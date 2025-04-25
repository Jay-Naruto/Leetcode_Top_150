from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minutes = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        fresh_org = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_org += 1
        if fresh_org == 0:
            return 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while q:
            level_rotted = False
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<= nx < m and 0<= ny < n and grid[nx][ny] == 1:
                        q.append((nx,ny))
                        fresh_org -= 1
                        grid[nx][ny] = 2
                        level_rotted = True
            if level_rotted:
                minutes += 1

        return minutes if fresh_org == 0 else -1