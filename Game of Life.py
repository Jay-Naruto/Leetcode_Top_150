class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 1 and len(board[0]) == 1:
            board[0][0] =  0
        dict=collections.defaultdict() # { [i,j] : live }
        for i in range(len(board)):
            for j in range(len(board[0])):
                dict[(i, j)] = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                    #right
                    if j < len(board[0])-1:
                        if board[i][j+1] == 1:
                            dict[(i, j)] += 1

                    #left
                    if j > 0:
                        if board[i][j-1] == 1:
                            dict[(i, j)] += 1
                    #up
                    if i > 0:
                        if board[i-1][j] == 1:
                            dict[(i, j)] += 1
                    #down
                    if i < len(board)-1:
                        if board[i+1][j] == 1:
                            dict[(i, j)] += 1
                    #topleft
                    if i > 0 and j > 0:
                        if board[i-1][j-1] == 1:
                            dict[(i, j)] += 1
                    #topright
                    if i > 0 and j < len(board[0])-1:
                        if board[i-1][j+1] == 1:
                            dict[(i, j)] += 1
                    #bottomright
                    if i < len(board)-1 and j < len(board[0])-1:
                        if board[i+1][j+1] == 1:
                            dict[(i, j)] += 1
                    #bottomleft
                    if i < len(board)-1 and j > 0:
                        if board[i+1][j-1] == 1:
                            dict[(i, j)] += 1
   
        for key, value in dict.items():
            row, col = key 
            # print(key,value)
            if board[row][col] == 1:  
                # Case 1
                if value < 2:
                    board[row][col] = 0
                # Case 2
                elif value == 2 or value == 3:
                    board[row][col] = 1
                # Case 3
                elif value > 3:
                    board[row][col] = 0
            else:
                # Case 4
                if value == 3:
                    board[row][col] = 1
