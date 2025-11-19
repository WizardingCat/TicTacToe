def print_board(board):
    '''prints out the board in the terminal'''
    count = 1
    for row in board:
        print(count, end="")
        for element in row:
            print(f"| {element} |", end = "")       
        print(end = "\n")
        count += 1
    print()


def check_row(n, board):
    '''returns True if the nth row is a winner'''
    for x in range(1, len(board[n])):
        if (board[n][0] != board[n][x]):
            return False        
    return True

    
def check_column(n, board):
    '''returns True if the nth column is a winner'''
    for x in range(1, len(board)):
        if (board[0][n] != board[x][n]):
            return False
    return True


def check_right_diag(board):
    '''returns True if the right diagonal is a winner'''
    for x in range(1, len(board)):
        if (board[0][0] != board[x][x]):
            return False
    return True


def check_left_diag(board):
    '''returns True if the left diagonal is a winner'''
    for x in range(len(board)):
        if(board[0][len(board) - 1] != board[x][len(board) - 1 - x]):
            return False
    return True


def check_board(board):
    '''returns True if there is a winner''' 
    if(check_left_diag(board) or check_right_diag(board)):
        return True

    else:
        for x in range(len(board)):
            if(check_column(x, board) or check_row(x, board)):
                return True 
        return False


def main():
    print("Welcome to TicTacToe")
    board_size = int(input("What size n do you want the nxn board to be:"))
    board = []
    for x in range(board_size): 
        row = []
        row.extend(["-"] * board_size)
        board.append(row)
    print_board(board)


if __name__ == "__main__":
    main()