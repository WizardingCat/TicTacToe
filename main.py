PLAYER_1 = "X"
PLAYER_2 = "O"

def print_board(board):
    '''prints out the board in the terminal'''
    num_row = list(range(1, len(board) + 1))
    count = 1
    print(" ", end = "")
    for element in num_row:
        print(f"  {element}  ", end="") 
    
    print("")
    for row in board:
        print(count, end="")
        for element in row:
            print(f"| {element} |", end = "")       
        print(end = "\n")
        count += 1
    print()


def check_row(n, board):
    '''returns True if the nth row is a winner'''
    if(board[0][n] == PLAYER_1 or board[0][n] == PLAYER_2):
        for x in range(1, len(board[n])):
            if (board[n][0] != board[n][x]):
                return False        
        return True
    else:
        return False

    
def check_column(n, board):
    '''returns True if the nth column is a winner'''
    if(board[0][n] == PLAYER_1 or board[0][n] == PLAYER_2):
        for x in range(1, len(board)):
            if (board[0][n] != board[x][n]):
                return False
        return True
    else:
        return False


def check_right_diag(board):
    '''returns True if the right diagonal is a winner'''
    if(board[0][0] == PLAYER_1 or board[0][0] == PLAYER_2):
        for x in range(1, len(board)):
            if (board[0][0] != board[x][x]):
                return False
        return True
    else:
        return False
    


def check_left_diag(board):
    '''returns True if the left diagonal is a winner'''
    if(board[0][len(board) - 1] == PLAYER_1 or board[0][len(board) - 1] == PLAYER_2):
        for x in range(len(board)):
            if(board[0][len(board) - 1] != board[x][len(board) - 1 - x]):
                return False
        return True
    else:
        return False


def check_board(board):
    '''returns True if there is a winner''' 
    if(check_left_diag(board) or check_right_diag(board)):
        return True

    else:
        for x in range(len(board)):
            if(check_column(x, board) or check_row(x, board)):
                return True 
        return False


def place_piece(row, column, board, player):
    '''returns the board with the player in the boards row and column'''
    board[row - 1][column - 1] = player
    return board


def switch_player(curr_player):
    '''returns the other player'''
    if (curr_player == PLAYER_1):
        return PLAYER_2
    else:
        return PLAYER_1



def main():
    print("Welcome to TicTacToe")
    board_size = int(input("What size n do you want the nxn board to be: "))
    board = []
    for x in range(board_size): 
        row = []
        row.extend(["-"] * board_size)
        board.append(row)
        
    print_board(board)
    print("Player 1 (X) will go first")
    curr_player = PLAYER_1

    while (not check_board(board)):
        used_spot = True
        column = None
        row = None
        
        while(used_spot):
            column = int(input(f"Which column do you want to enter you value player {curr_player} :"))
            row = int(input(f"Which row do you want to enter you value player {curr_player} :"))
            print()
            
            if(board[row - 1][column - 1] != PLAYER_1 and board[row - 1][column - 1] != PLAYER_2):
                used_spot = False

            else:
                print("Invalid position. Please reenter a position")

        print()
        board = place_piece(row, column, board, curr_player)
        print_board(board)
        curr_player = switch_player(curr_player)
        
    curr_player = switch_player(curr_player)
    print(f"Congrats {curr_player} you won!")

    
        
        



if __name__ == "__main__":
    main()