import pygame


class Square:
    def __init__(self, rank, file, width, height, occupying_piece) -> None:
        self.rank = rank
        self.file = file
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.rank * self.width, self.file * self.height, self.width, self.height)
        self.colour = (220, 208, 194) if (rank + file) % 2 == 0 else (53, 53, 53)
        self.highlight_colour = (0, 80, 0)
        self.occupying_piece = occupying_piece
        self.selected = False

    def draw(self, display):
        if self.selected == False:
            pygame.draw.rect(display, self.colour, self.rect)
        else:
            pygame.draw.rect(display, self.highlight_colour, self.rect)

        if self.occupying_piece != None:
            centre = self.occupying_piece.img.get_rect()
            centre.center = self.rect.center
            display.blit(self.occupying_piece.img, centre.topleft)
            #if selected, display potential moves

