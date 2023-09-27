import pygame
import math

class VectorAnimation:
    def __init__(self):
        self.WINDOW_DIM = (800, 600)  # width, height
        self.ARROW_LENGTH = 100
        self.ARROW_WIDTH = 15
        self.WHITE = (255, 255, 255)
        self.VECTOR_SOURCE = tuple(dim / 2 for dim in self.WINDOW_DIM)

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_DIM)
        pygame.display.set_caption("Direction Animation")

        self.font = pygame.font.Font(None, 36)  # Choose a font and size
        self.text_arr = []

    def set_text_arr(self, text_arr):
        self.text_arr = text_arr
    
    def update(self, angle):
        angle = -angle * math.pi/180
        self.screen.fill(self.WHITE)
        end_x = self.VECTOR_SOURCE[0] + self.ARROW_LENGTH * math.cos(angle)
        end_y = self.VECTOR_SOURCE[1] + self.ARROW_LENGTH * math.sin(angle)

        # Draw the arrow (line)
        pygame.draw.line(self.screen, (0, 0, 0), self.VECTOR_SOURCE, (end_x, end_y), 5)

        # Calculate arrowhead points with an adjusted angle
        arrowhead1_x = end_x + self.ARROW_WIDTH * math.cos(angle - math.pi / 6 + math.pi)
        arrowhead1_y = end_y + self.ARROW_WIDTH * math.sin(angle - math.pi / 6 + math.pi)
        arrowhead2_x = end_x + self.ARROW_WIDTH * math.cos(angle + math.pi / 6 + math.pi)
        arrowhead2_y = end_y + self.ARROW_WIDTH * math.sin(angle + math.pi / 6 + math.pi)

        # Draw the arrowhead (triangle)
        pygame.draw.polygon(self.screen, (0, 0, 0), [(end_x, end_y), (arrowhead1_x, arrowhead1_y), (arrowhead2_x, arrowhead2_y)])

        # Render and display heading and desired heading text
        for i in range(len(self.text_arr)):
            text = self.text_arr[i]
            rendered_text = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(rendered_text, (10, 10 + i * 40))

        # Update the display
        pygame.display.flip()