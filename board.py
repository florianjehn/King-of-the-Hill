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
        global width, height
        # initialize the screen
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("King of the Hill")
        # initialize pygame clock
        self.clock = pg.time.Clock()
    
    def update(self):
        """
        periodically updates the game, calls the graphics and receives user input
        """
        # sleep to make the game 60 fps
        self.clock.tick(60)
        
        # clear the screen
        self.screen.fill(0)
        
        # draw the board
        self.draw_board()
        
        for event in pg.event.get():
            # quit if the quit button was pressed
            if event.type == pg.QUIT:
                exit()
        
        #update the screen
        pg.display.flip()
        
    def draw_board(self):
        """
        calls all method which draw the seperate pieces of the board
        """
        global num_players, height, width
        center_rad = height/num_players/2
        ring_width = center_rad
        self.draw_center(center_rad)
        for player_num in range(num_players):
            self.draw_counter(player_num)
            self.draw_start_area(player_num)
            self.draw_ring(player_num, ring_width)
            
        
    
    def draw_center(self, center_rad):
        """
        draws the center piece
        """
        global height, width, WHITE
        pg.draw.circle(self.screen, WHITE, [width/2, height/2], center_rad)
    
    def draw_ring(self, player_num, ring_width):
        """
        draws the outer rings
        """
        global tiles_per_ring
        for tile in range(tiles_per_ring):
            self.draw_tile(player_num, ring_width)
        
    def draw_tile(self, player_num, ring_width):
        """ 
        draws one arc tile of a ring
        depending on the number of players and the size of the screen
        """
        pass
    
    def draw_counter(self, player_num):
        """
        draws the counters for the score of each player
        """
        
        pass
    
    def draw_start_area(self, player_num):
        """
        draws the starting area for each player
        """
    
    
num_players = 4
tiles_per_ring = 7
width = 800
height = 600
# Define the colors we will use in RGB format
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = (255, 0, 0)       
        
        
koth = KotH() # calls init
t = 1
while t < 500:
    koth.update()
    t += 1
    
pg.quit()
    