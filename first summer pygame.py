import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
SPEED = 50

# Create the game screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a player rect
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

def draw_screen():
    SCREEN.fill((0, 0, 0))
    pygame.draw.rect(SCREEN, (255, 0, 0), player)
    pygame.display.flip()

def handle_keys():
    # 1. Implement a way to quit the game when the user presses the escape key or closes the window
    # HINT: You can use pygame.event.get() to get a list of all events, and then iterate over that list to handle them with a for loop
        # HINT: use event.type to check for event handling, such as pygame.QUIT, pygame.KEYDOWN
        # HINT: use event.key to check for keyboard event, such as pygame.K_ESCAPE
        # HINT: logical operators will be useful in if statements for this
        # HINT: pygame.quit() and sys.exit() will quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    # Get a dictionary of key states
    key = pygame.key.get_pressed()
  

    # 2. Implement a way to move the player rect using the arrow keys
    # HINT: use the key variable to check what arrow key is pressed, ex: key[pygame.K_LEFT]
    # HINT: there will be 4 if statements 
    # HINT: use pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN to check which key
    # HINT: if left key is pressed, then player.move_ip(-SPEED, 0)
    # HINT: if right key is pressed, then player.move_ip(SPEED, 0)
    # HINT: if up key is pressed, then player.move_ip(0, -SPEED)
    # HINT: if down key is pressed, then  player.move_ip(0, SPEED)
    if key[pygame.K_LEFT]:
        player.move_ip(-SPEED, 0)
    if key[pygame.K_RIGHT]:
        player.move_ip(SPEED, 0)
    if key[pygame.K_UP]:
        player.move_ip(0, -SPEED)
    if key[pygame.K_DOWN]:
        player.move_ip(0, SPEED)

    # Keep the player rectangle on the screen
    if player.left < 0:
        player.left = 0
    elif player.right > WIDTH:
        player.right = WIDTH
    if player.top <= 0:
        player.top = 0
    elif player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def main():
    while True:
        handle_keys()
        draw_screen()

# Run the game
main()
