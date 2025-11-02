

def display_board(board): #Prints the board in a clear 3×3 layout
    print(f"{board[0]} | {board[1]} | {board[2]}\n---+---+---\n{board[3]} | {board[4]} | {board[5]}\n---+---+---\n{board[6]} | {board[7]} | {board[8]}")

# def player_move(player, board): #Asks player for a position and validates it 

# def check_winner(board): #Returns True if there’s a winner 

# def is_draw(board) #Returns True if the board is full and no one won 

# def switch_player(player): #Switches turn between "X" and "O"


board = ["X","O"," ","X","O","X"," ","O","X"]

display_board(board)
