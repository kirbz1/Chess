import pygame

class Board:
    def __init__(self) -> None:
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
        self.taken = []
        
    def generate_valid_moves(self, player):
        pass
