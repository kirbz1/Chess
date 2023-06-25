from Piece import Piece
import pygame

class Bishop(Piece):
    def __init__(self, colour, pos, board):
        super().__init__(colour, pos, board)
        self.img = pygame.image.load("resources/" + colour + "_bishop.png")
        self.img = pygame.transform.scale(self.img, (board.width/8, board.height/8))