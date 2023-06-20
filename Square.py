import pygame


class Square:
    def __init__(self, rank, file, width, height, occupying_piece) -> None:
        self.rank = rank
        self.file = file
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.rank * self.width, self.file * self.height, self.width, self.height)
        self.colour = (220, 208, 194) if (rank + file) % 2 == 0 else (53, 53, 53)
        self.occupying_piece = occupying_piece

    def draw(self, display):
        pygame.draw.rect(display, self.colour, self.rect)
        if self.occupying_piece != None:
            centre = self.occupying_piece.img.get_rect()
            centre.center = self.rect.center
            display.blit(self.occupying_piece.img, centre.topleft)

