class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        allRows=collections.defaultdict(set)
        allCols=collections.defaultdict(set)
        allSquares=collections.defaultdict(set)
        
        for r in range(9):
            
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    
                if (board[r][c] in allRows[r] or 
                    board[r][c] in allCols[c] or 
                    board[r][c] in allSquares[(r//3 , c//3)]):
                    return False
                
                allCols[c].add(board[r][c])
                allRows[r].add(board[r][c])
                allSquares[(r//3, c//3)].add(board[r][c])
        return True
        