import pygame


class Board:
    def __init__(self, width, height) -> None:
        self.board = [
            ["wR", "wKn", "wB", "wK", "wQ", "wB", "wKn", "wR"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bR", "bKn", "bB", "bK", "bQ", "bB", "bKn", "bR"]
        ]
        
        from Square import Square
        self.squares = []
        for i in range(8):
            for j in range(8):
                self.squares.append(Square(i, j, width/8, height/8))

        self.taken = []

    def draw(self, display):
        for square in self.squares:
            square.draw(display)

    def generate_valid_moves(self, player):
        pass
