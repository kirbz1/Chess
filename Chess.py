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
    player = "w"
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if board.left_click(mx, my, player) == 1:
                        if player == "w":
                            player = "b"
                        else:
                            player = "w"
                    
                    
        #if board.checkmate():
            #running = False
        draw(screen)