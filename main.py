def printBoard(board):
    '''prints out the board in the terminal'''
    pass


def checkBoard(board):
    '''returns True if there is a winner''' 


    def checkRow(n):
        '''returns True if the nth row is a winner'''
        for x in range(1, len(board[n])):
            if(board[n][0] != board[n][x]):
                return False        
        return True
    
    def checkColumn(n):
        '''returns True if the nth column is a winner'''
        for x in range(1, len(board)):
            if(board[0][n] != board[x][n]):
                return Falseg
        return True
                
    pass


def main():
    board = [[1, 2, 3],[4, 5, 6],[7, 8 ,9]]
    while(checkBoard):

        pass

if __name__ == "__main__":
    main()
