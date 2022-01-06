# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()
INITIAL_SCREEN_SIZE = 500

# Set up the drawing window
screen = pygame.display.set_mode([INITIAL_SCREEN_SIZE, INITIAL_SCREEN_SIZE])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board_image = pygame.image.load('./assets/board.jpg')
    screen.blit(pygame.transform.scale(board_image, (INITIAL_SCREEN_SIZE, INITIAL_SCREEN_SIZE)), (0, 0))
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
