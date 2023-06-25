import pygame

class Piece:
    def __init__(self, colour, pos, board) -> None:
        self.colour = colour
        self.pos = pos
        self.board = board