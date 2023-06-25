from Piece import Piece
import pygame

class Queen(Piece):
    def __init__(self, colour, pos, board):
        super().__init__(colour, pos, board)
        self.img = pygame.image.load("resources/" + colour + "_queen.png")
        self.img = pygame.transform.scale(self.img, (board.width/8, board.height/8))