from Piece import Piece
import pygame

class Pawn(Piece):
    def __init__(self, colour, pos, board):
        super().__init__(colour, pos, board)
        self.img = pygame.image.load("resources/" + colour + "_pawn.png")
        self.img = pygame.transform.scale(self.img, (board.width/8, board.height/8))

    
    def generate_moves(self):
        if self.colour == "w":
            sign = -1
        else:
            sign = 1
        
        #check square directly in front
        new_pos = (self.pos[0], self.pos[1] + 1 * (sign))
        new_square = self.board.get_square(new_pos)
        if new_square != None and new_square.occupying_piece == None:
            new_square.selected = True
            new_square.open = True
            #check square 2x ahead
            new_pos = (self.pos[0], self.pos[1] + 2 * (sign))
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
        #check if able to take an enemy piece
        new_pos = (self.pos[0] - 1, self.pos[1] + 1 * (sign))
        new_square = self.board.get_square(new_pos)
        if new_square != None and new_square.occupying_piece != None:
            if sign == -1 and new_square.occupying_piece.colour == "b":
                new_square.selected = True
                new_square.open = True
            elif sign == 1 and new_square.occupying_piece.colour == "w":
                new_square.selected = True
                new_square.open = True
        #check if able to take an enemy piece
        new_pos = (self.pos[0] + 1, self.pos[1] + 1 * (sign))
        new_square = self.board.get_square(new_pos)
        if new_square != None and new_square.occupying_piece != None:
            if sign == -1 and new_square.occupying_piece.colour == "b":
                new_square.selected = True
                new_square.open = True
            elif sign == 1 and new_square.occupying_piece.colour == "w":
                new_square.selected = True
                new_square.open = True
        
        #implement backrank change piece
        #implement en passant
