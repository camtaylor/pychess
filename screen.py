# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

class Screen:
    def __init__(self):
        self.cell_size = 64
        self.board_size = self.cell_size * 8
        self.display = pygame.display.set_mode([self.board_size, self.board_size])
        self.board_state = self.new_board_state()
        self.draw_board()


    def new_board_state(self):
        zero_row = [0 for i in range(8)]
        one_row = [1 for i in range(8)]
        back_row = [4,2,3,5,6,3,2,4]
        return [[-x for x in back_row], [-x for x in one_row],
        zero_row, zero_row, zero_row, zero_row,
        one_row, back_row][::-1]

    def draw_board(self):
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
            "-1": "./assets/pieces/lightpawn.png",
            "1": "./assets/pieces/darkpawn.png",
            "-2": "./assets/pieces/lightknight.png",
            "2": "./assets/pieces/darkknight.png",
            "-3": "./assets/pieces/lightbishop.png",
            "3": "./assets/pieces/darkbishop.png",
            "-4": "./assets/pieces/lightrook.png",
            "4": "./assets/pieces/darkrook.png",
            "-5": "./assets/pieces/lightqueen.png",
            "5": "./assets/pieces/darkqueen.png",
            "-6": "./assets/pieces/lightking.png",
            "6": "./assets/pieces/darkking.png",
            }
        piece_image = pygame.image.load(piece_filenames[str(piece_index)])
        piece_image = pygame.transform.scale(piece_image, (self.cell_size, self.cell_size))
        return piece_image

    def draw_pieces(self):
        for x in range(8):
            for y in range(8):
                piece = self.board_state[y][x]
                if piece != 0:
                    piece_image = self.load_piece(piece)
                    coordinates = self.get_square_coordinates(x,y)
                    self.display.blit(piece_image, [coordinates[0], coordinates[1]])


    def get_square_coordinates(self, x, y):
        return (x*self.cell_size, y*self.cell_size)


    def get_click(self, event):
        pos = pygame.mouse.get_pos()
        square = self.get_square(pos)
        self.highlight_square(square[0],square[1])

    def get_square(self, pos):
        x = pos[0]
        y = pos[1]
        return (x//self.cell_size, y//self.cell_size)

    def highlight_square(self, x, y):
        self.draw_board()
        pygame.draw.rect(self.board, (46,204,113), (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))
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
