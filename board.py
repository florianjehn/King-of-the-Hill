# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:43:16 2016

@author: Florian Jehn
"""

import pygame as pg

class KotH():
    def __init__(self):
        """
        define and call the screen for the game
        """
        pg.init()
        width = 800
        height = 600
        # initialize the screen
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("King of the Hill")
        # initialize pygame clock
        self.clock = pg.time.Clock()
    
    def update(self):
        """
        periodically updates the game, draws the graphics and receives user input
        """
        # sleep to make the game 60 fps
        self.clock.tick(60)
        
        # clear the screen
        self.screen.fill(0)
        
        for event in pg.event.get():
            # quit if the quit button was pressed
            if event.type == pg.QUIT:
                exit()
        
        #update the screen
        pg.display.flip()
        
koth = KotH() # calls init
while True:
    koth.update()
    