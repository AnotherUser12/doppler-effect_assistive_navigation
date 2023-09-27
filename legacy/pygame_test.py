import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ARROW_LENGTH = 100
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Animation")

# Initial position and angle of the arrow
x, y = WIDTH // 2, HEIGHT // 2
angle = 0  # Starting angle in radians
speed = 2  # Speed of rotation in radians per frame

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update the angle to make the arrow rotate
    angle += speed

    # Calculate the endpoint of the arrow
    end_x = x + ARROW_LENGTH * math.cos(angle)
    end_y = y + ARROW_LENGTH * math.sin(angle)

    # Draw the arrow
    pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 5)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()