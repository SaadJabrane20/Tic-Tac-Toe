from game import Board
def main():
    board = [" "," "," ",
             " "," "," ",
             " "," "," "]
    current_player = "X"
    game_over = False

    while not game_over:
        Board.display_board(Board)
        Board.player_move(current_player, Board)
        if Board.check_winner(Board) == True:
            Board.display_board(Board)
            print(f"The winner is {current_player}")
            game_over = True
        if Board.is_draw(Board):
            Board.display_board(Board)
            print("It's a draw !")
            game_over = True
        current_player = Board.switch_player(current_player)

if __name__ == "__main__":
    main()