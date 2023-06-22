import pygame

class Piece:
    def __init__(self, type, colour, width, height, pos, board) -> None:
        self.type = type
        self.colour = colour
        self.img = pygame.image.load("resources/" + colour + "_" + type + ".png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.pos = pos
        self.board = board

    def generate_moves(self):
        moves = []

        if self.type == "pawn":
            if self.colour == "w":
                sign = -1
            else:
                sign = 1

            new_pos = (self.pos[0], self.pos[1] + 1 * (sign))
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_pos = (self.pos[0], self.pos[1] + 2 * (sign))
                new_square = self.board.get_square(new_pos)
                if new_square != None and new_square.occupying_piece == None:
                    new_square.selected = True
            new_pos = (self.pos[0] - 1, self.pos[1] + 1 * (sign))
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece != None:
                if sign == -1 and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                elif sign == 1 and new_square.occupying_piece.colour == "w":
                    new_square.selected = True

                
 
            
            
        
        return moves
                    