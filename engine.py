import numpy as np
import game
import math

class Engine:

    def __init__(self):
        self.game = game.Game()

    def get_board_state(self):
        return self.game.board_state

    def get_turn(self):
        return self.game.turn

    def is_valid_piece(self, square):
        """
        Given a square, does that square contain a piece that can be moved,
        given the turn and the contents. Can't move 0, can't move opposite
        color of turn.

        :param square (tuple): Index of the board.
        :return valid (boolean): Is this a valid piece to move
        """

        board_state = self.get_board_state()

        piece = board_state[square[0], square[1]]
        if piece == 0:
            return False

        my_turn = math.log(piece, 2) % 2 == 0
        if my_turn == self.get_turn():
            return True
        else:
            return False



    def get_valid_moves(self, square):
        """

        Function that takes a index on the board and returns all
        the valid moves that piece can make given the type of piece.

        :param square (tuple): Tuple that holds the square's index ex. (0,1)
        :return valid_moves (list): List of tuples [squares] that the piece can move to
        """

        if square in self.game.valid_moves:
            self.make_move(self.game.selected_square, square)
            return []
        # This is not a valid piece
        if not self.is_valid_piece(square):
            return []

        valid_moves = []

        piece = self.get_board_state()[square[0], square[1]]
        #  White Pawn
        if piece == 1:
            valid_moves.append((square[0] - 1, square[1]))
            # If pawn on starting square, move two
            if square[0] == 6:
                valid_moves.append((square[0] - 2, square[1]))
            # TODO check diagonal for capture, or if blocked

        #  Black Pawn
        elif piece == 2:
            pass
        #  White Knight
        elif piece == 4:
            pass
        #  Black Knight
        elif piece == 8:
            pass
        #  White Bishop
        elif piece == 16:
            pass
        #  Black Bishop
        elif piece == 32:
            pass
        #  White Rook
        elif piece == 64:
            pass
        #  Black Rook
        elif piece == 128:
            pass
        #   White Queen
        elif piece == 256:
            pass
        #  Black Queen
        elif piece == 512:
            pass
        #  White King
        elif piece == 1024:
            pass
        #  Black King
        elif piece == 2048:
            pass

        self.game.valid_moves = valid_moves
        self.game.selected_square = square
        valid_moves.append(square)
        return valid_moves

    def make_move(self, from_square, to_square):
        piece = self.get_board_state()[from_square[0], from_square[1]]
        # Clear the from square
        self.game.board_state[from_square[0]][from_square[1]] = 0
        # Set the to square to the piece value
        self.game.board_state[to_square[0]][to_square[1]] = piece
        # Update Screen
        self.screen.draw_board()
        self.game.turn = not self.game.turn