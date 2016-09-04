# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:43:16 2016

@author: Florian Jehn
"""

import pygame as pg
import math
import time
import sys

class KotH():
    """
    main class for the game
    """
    # Define the colors we will use in RGB format as class attributes
    black = ( 0, 0, 0)
    white = (255, 255, 255)
    light_ter = ( 0, 255, 0) # green
    normal_ter = (255,255,0) # yellow
    diff_ter = (255, 0, 0) # red
    col_play_1 = ( 0, 0, 255) # blue
    col_play_2 = (186, 143, 43) # brown
    col_play_3 = (150, 43, 186) # purple
    col_play_4 = (177, 171, 179) # grey
    
    tiles = []
 
    
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
        
        # write something here that creates all tiles for the first time 
        # and sorts them into a list of list that represent all tile
        # sorted by the ring their in 
    
    def update(self):
        """
        periodically updates the game, calls the graphics and receives user input
        """
        # sleep to make the game 60 fps
        self.clock.tick(30)

        # make the screen white
        self.screen.fill(self.white)
        
        # draw the board
        self.draw_board()
        
        for event in pg.event.get():
            # quit if the quit button was pressed
            if event.type == pg.QUIT:
                pg.quit(); sys.exit()
        
        #update the screen
        pg.display.flip()
        
    def draw_board(self):
        """
        calls all method which draw the seperate pieces of the board
        """
        center_rad = (height//(num_players+3)//2) 
        ring_width = center_rad
        self.draw_center(center_rad)
        for player_num in range(num_players):
            self.draw_counter(player_num)
            self.draw_start_area(player_num)
            self.draw_ring(player_num, ring_width, center_rad)
            
        
    
    def draw_center(self, center_rad):
        """
        draws the center piece
        """
        # - 20 to adjust it in size        
        pg.draw.circle(self.screen, self.black, [width//2, height//2], center_rad-20)
    
    def draw_ring(self, player_num, ring_width, center_rad):
        """
        draws the outer rings
        """
        # draw all tiles
        for tile_num in range(tiles_per_ring):
            self.draw_tile(player_num, ring_width, tile_num, center_rad)
        
    def draw_tile(self, player_num, ring_width, tile_num, center_rad):
        """ 
        draws one arc tile of a ring
        depending on the number of players and the size of the screen
        """
        # calculate distance of the rectangle of the arc from the center
        distance = (player_num*ring_width)+ 0.5*ring_width + center_rad
        # draw arcs, each 2*pi/7 wide
        pg.draw.arc(self.screen, self.black, [0.5*width-distance, 0.5*height-distance, distance*2, distance*2], tile_num*(2*pi/7), (tile_num*(2*pi/7))+2*pi/7, int(ring_width*0.5))   
        
        
    
    def draw_counter(self, player_num):
        """
        draws the counters for the score of each player
        """
        
        pass
    
    def draw_start_area(self, player_num):
        """
        draws the starting area for each player
        """
        pass

class Tile:
    """
    class for the instances of the tiles on the board
    """
    def __init__(self, rect_x = 0, rect_y = 0 , terrain = 0):
        """
        defines the instance attributes for every tile on call
        """
        # terrain 0 = black, 1 = light/green, 2 normal/yellow, 3 difficult/red
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.terrain = terrain
        
    def change_terrain(self, new_ter):
        """changes the terrain"""
        self.terrain = new_ter
        
class Counter:
    """
    class for the instances of the counters
    """
    def __init__(self, x = 0, y = 0, player = None, points = 0):
        """
        defines the instance attributes for every counter on call
        """
        self.x = x
        self.y = y
        self.player = player
        self.points = points
        
    def increment_points(self):
        """increments the points by one"""
        self.points += 1
        
class Start_Area:
    """
    class for the instances of the starting areas
    """
    def __init__(self, rect_x = 0, rect_y = 0, player = None):
        """
        defines the instance attributes for every start area on call
        """
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.player = player
        
# Important variables
        
num_players = 4
tiles_per_ring = 7
width = 800
height = 800
pi = math.pi

   
        
 
if __name__ == "__main__":       
    koth = KotH() # calls init
    
    while True:
        koth.update()
        
    pg.quit()
    