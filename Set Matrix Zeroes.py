class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visitedIndex=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visitedIndex.append([i,j])
        k=0
        for visited in visitedIndex:
                    k=visited[1]
                    while k < len(matrix[0]):
                        matrix[visited[0]][k] = 0
                        k+=1
                    k=visited[1]
                    while k >= 0:
                        matrix[visited[0]][k] = 0
                        k-=1
                    k=visited[0]
                    while k >= 0:
                        matrix[k][visited[1]] = 0
                        k-=1
                    k=visited[0]
                    while k < len(matrix):
                        matrix[k][visited[1]] = 0
                        k+=1

        