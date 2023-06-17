import pygame
import Board

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.forward = []
        self.backward = []
        self.active_player = "W"

    def move(self):
        

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
        