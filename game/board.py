#Prints the board in a clear 3×3 layout
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n---+---+---\n{board[3]} | {board[4]} | {board[5]}\n---+---+---\n{board[6]} | {board[7]} | {board[8]}")

def switch_player(player): #Switches turn between "X" and "O"
    if player == "X":
        return "O"
    elif player == "O":
        return "X"
    
#Asks player for a position and validates it 
def player_move(player, board):
   while True:
        try:
            n = int(input(f"Player {player}, enter a position [1-9]: "))
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        if n < 1 or n > 9:
            print("Position out of range. Choose another position.")
            continue

        if board[n - 1] != " ":
            print("Position already taken. Choose another position.")
            continue

        # Valid move
        board[n - 1] = player
        break
   
#Returns True if there’s a winner 
def check_winner(board): 
    winning_combinations = [
    (0, 1, 2),  # rows
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),  # columns
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),  # diagonals
    (2, 4, 6)
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board [b] == board[c] != " ":
            return True
        
    return False

#Returns True if the board is full and no one won
def is_draw(board):
    for i in range (0, 9):
        if board[i] == " ":
            return False
    return True
