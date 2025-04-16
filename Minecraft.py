import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Minecraft")

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define block size
BLOCK_SIZE = 20

# Define the player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 5
        self.width = 30
        self.height = 40

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Define the block class
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

# Create the player
player = Player(window_size[0] // 2, window_size[1] - 100)

# Create blocks
blocks = []
for y in range(0, window_size[1], BLOCK_SIZE):
    for x in range(0, window_size[0], BLOCK_SIZE):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        blocks.append(Block(x, y, color))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_LEFT]:
        player.move(-player.velocity, 0)
    if keys[pygame.K_RIGHT]:
        player.move(player.velocity, 0)
    if keys[pygame.K_UP]:
        player.move(0, -player.velocity)
    if keys[pygame.K_DOWN]:
        player.move(0, player.velocity)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the blocks
    for block in blocks:
        block.draw(screen)

    # Draw the player
    player.draw(screen)

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()