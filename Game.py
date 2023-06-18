import pygame
import Board

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.forward = []
        self.backward = []
        self.active_player = "W"
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
        