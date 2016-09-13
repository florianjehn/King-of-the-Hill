# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:03:17 2016

@author: Florian Jehn
"""

import mechanics as mec
import board
import pygame as pg
import sys

 


def update(board):
    """
    periodically updates the game, calls the graphics and receives user input
    """
    # sleep to make the game 60 fps
    board.clock.tick(30)

    # make the screen white
    board.screen.fill(board.white)
    
    # draw the board
    board.draw_board()
    
    for event in pg.event.get():
        # quit if the quit button was pressed
        if event.type == pg.QUIT:
            pg.quit(); sys.exit()
    
    #update the screen
    pg.display.flip()
    
    
if __name__ == "__main__":       
    koth = board.Board() # calls init
    
    while True:
        update(koth)
        
    pg.quit()
    