class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans, sol= [], []
        def helper(i,j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False

            temp = board[i][j] 
            board[i][j] = "#"
            final = (helper(i+1,j, idx+1) or
                    helper(i,j+1, idx+1) or
                    helper(i-1,j, idx+1) or
                    helper(i,j-1, idx+1))
            board[i][j] = temp
            return final

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and helper(i,j, 0):
                    return True
        return False
        