import pygame
import Board

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.forward = []
        self.backward = [] #make deepcopy of board positions and add to forward/backward arrays
        self.active_player = "w"
        self.white_timer = 600
        self.black_timer = 600
        self.white = None
        self.black = None

    def move(self):
        self.board.generate_valid_moves(self.active_player)

    def forward(self):
        if len(self.forward) == 0:
            print("Not possible to go forward")
        
        self.backward.append(self.board)
        self.board = self.forward.pop()
         
    def backward(self):
        if len(self.backward == 0):
            print("Not possible to go backward")
        
        self.forward.append(self.board)
        self.board = self.backward.pop()
        