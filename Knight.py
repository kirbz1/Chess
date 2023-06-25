from Piece import Piece
import pygame

class Knight(Piece):
    def __init__(self, colour, pos, board):
        super().__init__(colour, pos, board)
        self.img = pygame.image.load("resources/" + colour + "_knight.png")
        self.img = pygame.transform.scale(self.img, (board.width/8, board.height/8))

    
    def generate_moves(self):
        
        def check_square():
            if new_square != None:
                if new_square.occupying_piece == None or new_square.occupying_piece.colour != self.colour:
                    new_square.selected = True
                    new_square.open = True

        new_pos = (self.pos[0] + 1, self.pos[1] + 2)
        new_square = self.board.get_square(new_pos)
        check_square()

        new_pos = (self.pos[0] + 1, self.pos[1] - 2)
        new_square = self.board.get_square(new_pos)
        check_square()

        new_pos = (self.pos[0] - 1, self.pos[1] + 2)
        new_square = self.board.get_square(new_pos)
        check_square()

        new_pos = (self.pos[0] - 1, self.pos[1] - 2)
        new_square = self.board.get_square(new_pos)
        check_square()

        new_pos = (self.pos[0] + 2, self.pos[1] + 1)
        new_square = self.board.get_square(new_pos)
        check_square()

        new_pos = (self.pos[0] - 2, self.pos[1] + 1)
        new_square = self.board.get_square(new_pos)
        check_square()

        new_pos = (self.pos[0] + 2, self.pos[1] - 1)
        new_square = self.board.get_square(new_pos)
        check_square()

        new_pos = (self.pos[0] - 2, self.pos[1] - 1)
        new_square = self.board.get_square(new_pos)
        check_square()