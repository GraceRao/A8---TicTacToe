# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game, Player, Bot

def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print_row = [cell if cell is not None else ' ' for cell in row]
        print(f"{i} {' '.join(print_row)}")

def main():
    mode = input("Choose mode (1 for single player, 2 for two players): ")
    player1 = Player('X')
    player2 = Bot('O') if mode == '1' else Player('O')

    game = Game(player1, player2)

    while True:
        print_board(game.board)
        game.play_turn()
        winner = game.get_winner()
        if winner:
            print_board(game.board)
            print(f"Player {winner} wins!")
            break
        if game.is_draw():
            print_board(game.board)
            print("It's a draw!")
            break

if __name__ == '__main__':
    main()