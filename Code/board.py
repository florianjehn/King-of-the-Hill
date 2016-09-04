# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:43:16 2016

@author: Florian Jehn
"""

import pygame as pg
import math
import datetime
import time
import random
import sys
import copy

class board():
    """
    draws all the things needed to start and play the game
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
    
    tile_colors = [black, light_ter, normal_ter, diff_ter]
    player_colors =  [col_play_1, col_play_2, col_play_4, col_play_4]
    
    # define the terrains
    ter_names = ["center", "light", "normal", "difficult"]
    
    # define the units
    unit_names = ["runner", "warrior", "blocker"]
    
    # prepare the tiles list of list for all tiles
    tiles = []
    for section in range(6):
        tiles.append([])
 
    # define additional class attributes
    center_rad = (height//7//2) 
    ring_width = center_rad

    
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
        
        # Order of tiles in the tiles list of lists
        # tiles [0] = most inward ring
        # tiles [1] = second most inward ring
        # tiles [2] = third most inward ring
        # tiles [3] = outer ring
        # tiles [4] = center piece
        # tiles [5] = starting areas
        self.tiles[4].append(Center_Piece(width//2, height//2, self.center_rad-20))
        terrains = self.init_terrain()
        for ring in range(4):
            for tile in range(6):
                self.tiles[ring].append(Tile())

    def init_terrain(self):
        """
        creates and returns a list of list which contains the randomized terrain
        for all tiles of ring
        """
        terrains = []
        ring = [1,1,1,2,2,3,3]            
        for ring_num in range(4):
            ring_copy = copy.copy(ring)
            random.shuffle(ring_copy) # shuffle it, so that the starting order of terrains is random for every ring              
            terrains.append(ring_copy)             
        return terrains
    
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
        self.draw_center()
        for player_num in range(num_players):
            self.draw_counter(player_num)
            self.draw_start_area(player_num)
            # number of players is also four therefore draw_ring can be called here also
            self.draw_ring(player_num) 
            
        
    
    def draw_center(self):
        """
        draws the center piece
        """
        # - 20 to adjust it in size        
        pg.draw.circle(self.screen, self.black, [self.tiles[4][0].x, self.tiles[4][0].y], self.tiles[4][0].rad)
    
    def draw_ring(self, player_num):
        """
        draws the outer rings
        """
        # draw all tiles
        for tile_num in range(tiles_per_ring):
            self.draw_tile(player_num, tile_num)
        
    def draw_tile(self, player_num, tile_num):
        """ 
        draws one arc tile of a ring
        depending on the number of players and the size of the screen
        """
        # calculate distance of the rectangle of the arc from the center
        distance = (player_num*self.ring_width)+ 0.5*self.ring_width + self.center_rad
        # draw arcs, each 2*pi/7 wide
        pg.draw.arc(self.screen, self.black, [0.5*width-distance, 0.5*height-distance, distance*2, distance*2], tile_num*(2*pi/7), (tile_num*(2*pi/7))+2*pi/7, int(self.ring_width*0.5))   
        
        
    
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
    
    def rotate_ring_right(self, ring_num):
        """
        rotates a ring one field to the right
        """
        # to accomplish this save the pos of the first tile in the ring
        # in a temporary variable, then interchange clockwise the position data 
        # of all tiles
        pass 
   
    def rotate_ring_left(self, ring_num):
        """
        rotates a ring one field to the right
        """
        pass

class Tile:
    """
    class for the instances of the tiles on the board
    """
    
    # Somehow the units must be asociated with a given tile
    
    
    # define the terrains
    ter_names = ["center", "light", "normal", "difficult"]

    
    def __init__(self, rect_x = 0, rect_y = 0 ,radi_start = 0, radi_end = 0,  terrain = 0):
        """
        defines the instance attributes for every tile on call
        """
        # terrain 0 = black (center), 1 = light/green, 2 normal/yellow, 3 difficult/red
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.radi_start = radi_start
        self.radi_end = radi_end
        self.terrain = terrain
        
    def __str__(self):
        pass
        
    def change_terrain(self, new_ter):
        """changes the terrain"""
        self.terrain = new_ter
        
    def change_pos(self, new_radi_start, new_radi_end):
        """
        changes the position of a tile
        """
        self.radi_start = new_radi_start
        self.radi_end = new_radi_end
        
class Center_Piece:
    """
    class for the instance of the center piece
    """
    def __init__(self,x = 0, y = 0, rad = 0, col = 0):
        """
        defines the instance attributes
        """
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        
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
        
    def increment(self):
        """increments the points by one"""
        self.points += 1
        
class Start_Area:
    """
    class for the instances of the starting areas
    """
    def __init__(self, rect_x = 0, rect_y = 0, radi_start = 0, radi_end = 0, player = None):
        """
        defines the instance attributes for every start area on call
        """
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.radi_start = radi_start
        self.radi_end = radi_end
        self.player = player
        
    def change_pos(self, new_radi_start, new_radi_end):
        """
        changes the position of the start are
        """
        self.radi_start = new_radi_start
        self.radi_end = new_radi_end
        
class Unit:
    # 0 = runner, 1 = warrior, 2 = blocker
    # define the units
    unit_names = ["runner", "warrior", "blocker"]    
    pass
        
# Important variables
        
num_players = 4
tiles_per_ring = 7
width = 800
height = 800
pi = math.pi

   
        
 
if __name__ == "__main__":       
    koth = board() # calls init
    
    while True:
        koth.update()
        
    pg.quit()
    