import numpy as np

class Game:
    def __init__(self):
        self.board_state = self.new_board()
        self.turn = True
        self.valid_moves = []
        self.selected_square = ()



    def new_board(self):
        board = np.zeros((8,8), np.uint16)
        back_row = [6, 2, 4, 8, 10, 4, 2, 6]
        white_encode = lambda x: 2 ** x
        black_encode = lambda x: 2 ** (x+1)
        board[7] = [white_encode(back_row[i]) for i in range(8)]
        board[0] = [black_encode(back_row[i]) for i in range(8)]
        board[6] = [white_encode(0) for i in range(8)]
        board[1] = [black_encode(0) for i in range(8)]
        return board


if __name__ == "__main__":
    game = Game()
    print(game.board_state)