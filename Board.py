import pygame
from Piece import Piece

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

                if  j == 1 or j == 6:
                    piece = Piece("pawn", colour, square_width, square_height, (i,j))
                    self.squares.append(Square(i, j, square_width, square_height, piece))
                elif j > 1 and j < 6:
                    self.squares.append(Square(i, j, square_width, square_height, None))
                elif i == 0 or i == 7:
                    piece = Piece("rook", colour, square_width, square_height, (i,j))
                    self.squares.append(Square(i, j, square_width, square_height, piece))
                elif i == 1 or i == 6:
                    #black knight
                    piece = Piece("knight", colour, square_width, square_height, (i,j))
                    self.squares.append(Square(i, j, square_width, square_height, piece))
                elif i == 2 or i == 5:
                    #black bishop
                    piece = Piece("bishop", colour, square_width, square_height, (i,j))
                    self.squares.append(Square(i, j, square_width, square_height, piece))
                elif i == 4:
                    #black king
                    piece = Piece("king", colour, square_width, square_height, (i,j))
                    self.squares.append(Square(i, j, square_width, square_height, piece))
                elif i == 3:
                    #black queen
                    piece = Piece("queen", colour, square_width, square_height, (i,j))
                    self.squares.append(Square(i, j, square_width, square_height, piece))
                

                    



    def draw(self, display):
        for square in self.squares:
            square.draw(display)

    def get_square_from_xy(self, x, y):
        square_width = self.width/8
        square_height = self.height/8
        for square in self.squares:
            if square.rank == int(x // square_width) and square.file == int(y // square_height):
                
               
                if self.highlighted != None and self.highlighted.rank == square.rank and self.highlighted.file == square.file:
                    square.selected = False
                    self.highlighted = None

                elif self.highlighted != None:         
                    self.highlighted.selected = False
                    square.selected = True
                    self.highlighted = square

                else:
                    square.selected = True
                    self.highlighted = square
                


