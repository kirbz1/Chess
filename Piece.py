import pygame

class Piece:
    def __init__(self, type, colour, width, height, pos) -> None:
        self.type = type
        self.colour = colour
        self.img = pygame.image.load("resources/" + colour + "_" + type + ".png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.pos = pos

    def generate_moves(self):
        moves = []

        if self.type == "pawn":
            
            moves = [(0,1), (0,2), (-1,1), (1,1)]
        
        return moves
                    