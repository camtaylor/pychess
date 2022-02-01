# Simple pygame program

# Import and initialize the pygame library
import pygame
import engine
pygame.init()

class Screen:

    def __init__(self):
        self.cell_size = 64
        self.board_size = self.cell_size * 8
        self.engine = engine.Engine()
        self.engine.screen = self
        self.display = pygame.display.set_mode([self.board_size, self.board_size])
        self.draw_board()
        self.piece_selected = False


    def get_board_state(self):
        """
        Functuion to return the board state (list of lists) from the engine
        :return:
        """
        return self.engine.get_board_state()

    def draw_board(self):
        """
         Drawing the background board itself, under the pieces.
        :return:
        """
        self.board = pygame.Surface((self.cell_size * 8, self.cell_size * 8))
        self.board.fill((20, 93, 160))

        for x in range(0, 8, 1):
            for y in range(0, 8, 2):
                y_position = self.cell_size*y
                if x % 2 != 0:
                    y_position += self.cell_size
                pygame.draw.rect(self.board, (255,255,255), (x*self.cell_size, y_position, self.cell_size, self.cell_size))
        self.display.blit(self.board, self.board.get_rect())
        self.draw_pieces()

    def load_piece(self, piece_index):
        piece_filenames = {
            "1": "./assets/pieces/lightpawn.png",
            "2": "./assets/pieces/darkpawn.png",
            "4": "./assets/pieces/lightknight.png",
            "8": "./assets/pieces/darkknight.png",
            "16": "./assets/pieces/lightbishop.png",
            "32": "./assets/pieces/darkbishop.png",
            "64": "./assets/pieces/lightrook.png",
            "128": "./assets/pieces/darkrook.png",
            "256": "./assets/pieces/lightqueen.png",
            "512": "./assets/pieces/darkqueen.png",
            "1024": "./assets/pieces/lightking.png",
            "2048": "./assets/pieces/darkking.png",
            }
        piece_image = pygame.image.load(piece_filenames[str(piece_index)])
        piece_image = pygame.transform.scale(piece_image, (self.cell_size, self.cell_size))
        return piece_image

    def draw_pieces(self):
        """
        Function that gets the board state and draws the pieces on the board
        :return:
        """
        board_state = self.get_board_state()
        for x in range(8):
            for y in range(8):
                piece = board_state[x][y]
                if piece != 0:
                    piece_image = self.load_piece(piece)
                    coordinates = self.get_square_coordinates(y,x)
                    self.display.blit(piece_image, [coordinates[0], coordinates[1]])


    def get_square_coordinates(self, x, y):
        return (x*self.cell_size, y*self.cell_size)


    def get_click(self, event):
        pos = pygame.mouse.get_pos()
        square = self.get_square(pos)
        self.select_square((square[0],square[1]))

    def get_square(self, pos):
        x = pos[1]
        y = pos[0]
        square = (x//self.cell_size, y//self.cell_size)
        return square

    def select_square(self, square):
        """

        Function to display highlighted piece and all possible moves for that piece.

        :param square (tuple): The index of the square as a tuple
        :return None:
        """

        # Getting valid moves from the engine
        moves = self.engine.get_valid_moves(square)
        # Highlight moves and square
        self.highlight_squares(moves)



    def highlight_squares(self, squares):
        """
        Function that highlights a list of squares.

        :param squares (list): List of tuples to highlight
        :return None:
        """

        self.draw_board()

        for square in squares:

            contains_piece = self.get_board_state()[square[0], square[1]] != 0
            y = square[0]
            x = square[1]

            # If square contains a piece, draw rectangle
            if contains_piece:
                pygame.draw.rect(self.board, (46, 204, 113),
                                 (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                self.display.blit(self.board, self.board.get_rect())
            # Else draw a dot
            else:
                pygame.draw.circle(self.board, (46, 204, 113),
                         (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2), self.cell_size // 8)
                self.display.blit(self.board, self.board.get_rect())
        self.draw_pieces()


# Run until the user asks to quit
running = True
screen = Screen()
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.get_click(event)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
