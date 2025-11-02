from game import Board
def main():
    board = [" "," "," ",
             " "," "," ",
             " "," "," "]
    current_player = "X"
    game_over = False

    while not game_over:
        Board.display_board(board)
        Board.player_move(current_player, board)
        if Board.check_winner(board) == True:
            Board.display_board(board)
            print(f"The winner is {current_player}")
            game_over = True
        if Board.is_draw(board):
            Board.display_board(board)
            print("It's a draw !")
            game_over = True
        current_player = Board.switch_player(current_player)

if __name__ == "__main__":
    main()