import pygame
import Game
from Board import Board


pygame.init()
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(600, 600)

def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()



if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen)