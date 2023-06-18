import pygame

class Square:
    def __init__(self, rank, file, width, height) -> None:
        self.rank = rank
        self.file = file
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.rank * self.width, self.file * self.height, self.width, self.height)
        self.colour = (220, 208, 194) if (rank + file) % 2 == 0 else (53, 53, 53)
        self.occupying_piece = None

    def draw(self, display):
        pygame.draw.rect(display, self.colour, self.rect)
