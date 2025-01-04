class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m,n = len(matrix) ,len(matrix[0])
        l=0
        r=m*n -1
        while l <=r :
                m = (l+r) // 2
                row = m // n
                col = m % n
                mid = matrix[row][col]
                if mid == target:
                    return True
                elif target > mid:
                    l=m+1
                else:
                    r=m-1

        return False
        