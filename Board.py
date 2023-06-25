import pygame
from Piece import Piece
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Queen import Queen
from King import King
from Bishop import Bishop

class Board:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
        square_width = width/8
        square_height = height/8
        self.highlighted = None

        from Square import Square
        
        self.squares = []
        
        for i in range(8):
            for j in range(8):
                
                if j < 2:
                    colour = "b"
                else:
                    colour = "w"

                if j == 3 and i == 4:
                    piece = King(colour, (i,j), self)
                elif  j == 1 or j == 6:
                    piece = Pawn(colour, (i,j), self)
                elif j > 1 and j < 6:
                    piece = None
                elif i == 0 or i == 7:
                    piece = Rook(colour, (i,j), self)
                elif i == 1 or i == 6:
                    piece = Knight(colour, (i,j), self)
                elif i == 2 or i == 5:
                    piece = Bishop(colour, (i,j), self)
                elif i == 4:
                    piece = King(colour, (i,j), self)
                elif i == 3:
                    piece = Queen(colour, (i,j), self)
                
                self.squares.append(Square(i, j, square_width, square_height, piece, (i,j)))
                

                    



    def draw(self, display):
        for square in self.squares:
            square.draw(display)

    def get_square(self, pos):
        for square in self.squares:
            if square.pos == pos:
                return square
        return None

    def get_square_from_xy(self, x, y):
        
        for square in self.squares:
            
            if square.rank == int( x // (self.width / 8) ) and square.file == int( y // (self.height / 8) ):
                
                if square.open == True:
                    square.occupying_piece = self.highlighted.occupying_piece

        for square in self.squares:
            square.selected = False
            square.open = False
        
        for square in self.squares:
            
            if square.rank == int( x // (self.width / 8) ) and square.file == int( y // (self.height / 8) ):
                
                

                if self.highlighted != None and self.highlighted.rank == square.rank and self.highlighted.file == square.file:
                    square.selected = False
                    self.highlighted = None

                elif self.highlighted != None:         
                    self.highlighted.selected = False
                    square.selected = True
                    self.highlighted = square
                    if square.occupying_piece != None:
                        square.occupying_piece.generate_moves()

                else:
                    square.selected = True
                    self.highlighted = square
                    if square.occupying_piece != None:
                        square.occupying_piece.generate_moves()
