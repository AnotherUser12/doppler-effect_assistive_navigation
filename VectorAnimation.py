import pygame
import math

class VectorAnimation:
    def __init__(self):
        self.WINDOW_DIM = (800,600) #width, height
        self.ARROW_LENGTH = 100
        self.WHITE = (255,255,255)
        self.VECTOR_SOURCE = tuple(dim / 2 for dim in self.WINDOW_DIM)

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_DIM)
        pygame.display.set_caption("Direction  Animation")
    
    def update(self, angle):
        self.screen.fill(self.WHITE)
        end_x = self.VECTOR_SOURCE[0] + self.ARROW_LENGTH * math.cos(angle)
        end_y = self.VECTOR_SOURCE[1] + self.ARROW_LENGTH * math.sin(angle)

        # Draw the arrow
        pygame.draw.line(self.screen, (0, 0, 0), self.VECTOR_SOURCE, (end_x, end_y), 5)

        # Update the display
        pygame.display.flip()
