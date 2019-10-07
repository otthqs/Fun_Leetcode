class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(i,j,board):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = '#'

            bfs(i+1,j,board)
            bfs(i-1,j,board)
            bfs(i,j-1, board)
            bfs(i,j+1, board)

        if not board:
            return board

        #从外层开始搜索起来，遇到'O'进入循环，从外层O搜索到的O均为未包围
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            if board[i][0] == 'O': bfs(i,0,board)
            if board[i][cols-1] == 'O': bfs(i,cols-1,board)

        for j in range(cols):
            if board[0][j] == 'O': bfs(0,j,board)
            if board[rows-1][j] == 'O' : bfs(rows-1,j,board)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != '#':
                    board[i][j] = 'X'

                else:
                    board[i][j] = 'O'


        
