class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        flat_arr=[-1] * (n*n)
        i=0
        for r in range(n-1, -1, -1):
            if (n-r)%2 == 1:
                for c in range(n):
                    flat_arr[i] = board[r][c]
                    i+=1
            else:
                for c in range(n-1,-1,-1):
                    flat_arr[i] = board[r][c]
                    i+=1
        
        q=deque([(0,0)])
        visited=[False]*(n*n)
        visited[0]=True

        while q:
            curr,rolls=q.popleft()
            for dice in range(1,7):
                next_sq = curr+dice

                if next_sq >= n*n:
                    continue
                if flat_arr[next_sq] != -1:
                    next_sq = flat_arr[next_sq]-1
                if next_sq == n*n - 1:
                    return rolls+1
                if not visited[next_sq]:
                    visited[next_sq]=True
                    q.append((next_sq, rolls+1))
        return -1
                

        