from Piece import Piece
import pygame

class Queen(Piece):
    def __init__(self, colour, pos, board):
        super().__init__(colour, pos, board)
        self.img = pygame.image.load("resources/" + colour + "_queen.png")
        self.img = pygame.transform.scale(self.img, (board.width/8, board.height/8))

    def generate_moves(self):
        
        for i in range(1,9):
            new_pos = (self.pos[0], self.pos[1] + i)
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break

        for i in range(1,9):
            new_pos = (self.pos[0], self.pos[1] - i)
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break

        for i in range(1,9):
            new_pos = (self.pos[0] + i, self.pos[1])
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break
        
        for i in range(1,9):
            new_pos = (self.pos[0] - i, self.pos[1])
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break

        for i in range(1,9):
            new_pos = (self.pos[0] + i, self.pos[1] + i)
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break

        for i in range(1,9):
            new_pos = (self.pos[0] - i, self.pos[1] - i)
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break

        for i in range(1,9):
            new_pos = (self.pos[0] + i, self.pos[1] - i)
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break
        
        for i in range(1,9):
            new_pos = (self.pos[0] - i, self.pos[1] + i)
            new_square = self.board.get_square(new_pos)
            if new_square != None and new_square.occupying_piece == None:
                new_square.selected = True
                new_square.open = True
            elif new_square != None and new_square.occupying_piece != None:
                if self.colour == "w" and new_square.occupying_piece.colour == "b":
                    new_square.selected = True
                    new_square.open = True
                elif self.colour == "b" and new_square.occupying_piece.colour == "w":
                    new_square.selected = True
                    new_square.open = True
                break
            else:  
                break