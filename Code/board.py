# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:43:16 2016

@author: Florian Jehn
"""

import pygame as pg
import math
import random
import copy
import circular_arc as ca

class Board():
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
    
    # order the colors for easier access
    tile_colors = [black, light_ter, normal_ter, diff_ter]
    player_colors =  [col_play_1, col_play_2, col_play_4, col_play_4]
    
    # prepare the tiles list of list for all tiles
    # explanation of order in __init__
    tiles = []
    for section in range(6):
        tiles.append([])
 
    # define additional class attributes
    width = 800
    height = 800
    center_rad = (height//7//2) 
    ring_width = center_rad        
    num_players = 4
    num_rings = 4
    tiles_per_ring = 7
    
    def __init__(self):
        """
        define and call the screen for the game
        """
        pg.init()
        global width, height
        # initialize the screen
        self.screen = pg.display.set_mode((self.width, self.height))
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
        
        # reshuffle the terrain for each ring
        
        terrains = self.shuffle_terrain()
        # add all ring tiles        
        for ring in range(self.num_rings):
            for tile in range(self.tiles_per_ring):
                # calculate distance of the rectangle of the arc (tile) from the center
                distance = (ring*self.ring_width)+ 0.5*self.ring_width + self.center_rad
                rect_x = 0.5*self.width-distance
                rect_y = 0.5*self.height-distance
                rect_height = distance * 2
                rect_width = distance * 2
                # each arc is 2*pi/7 wide
                radi_start = tile*(2*math.pi/7)
                radi_end = (tile*(2*math.pi/7))+2*math.pi/7
                terrain = terrains[ring][tile]
                ring_width = int(self.ring_width*0.5)

                self.tiles[ring].append(Tile(rect_x, rect_y, rect_height, rect_width, radi_start, radi_end, terrain, ring_width)) 
        
        # add center
        self.tiles[4].append(Center_Piece(self.width//2, self.height//2, self.center_rad-20))
        
        # add starting areas
        # self.tiles[5].append(Starting_Area())
    

    def shuffle_terrain(self):
        """
        creates and returns a list of list which contains the randomized terrain
        for all tiles of a ring
        """
        terrains = []
        ring = [1,1,1,2,2,3,3]            
        for ring_num in range(4):
            ring_copy = copy.copy(ring)
            random.shuffle(ring_copy) # shuffle it, so that the starting order of terrains is random for every ring              
            terrains.append(ring_copy)             
        return terrains
    
        
    def draw_board(self):
        """
        calls all method which draw the seperate pieces of the board
        """
        self.draw_center()
        for ring in range(self.num_rings):
            self.draw_ring(ring)        
        
        for player_num in range(self.num_players):
            self.draw_counter(player_num)
            self.draw_start_area(player_num)            
    
    def draw_center(self):
        """
        draws the center piece
        """
        # - 20 to adjust it in size        
        pg.draw.circle(self.screen, self.black, [self.tiles[4][0].x, self.tiles[4][0].y], self.tiles[4][0].rad)
    
    def draw_ring(self, ring):
        """
        draws the outer rings
        """
        # draw all tiles
        for tile in range(self.tiles_per_ring):
            self.draw_tile(tile, ring)
        
    def draw_tile(self, tile, ring):
        """ 
        draws one arc tile of a ring
        depending on the number of players and the size of the screen
        """
        pg.draw.arc(self.screen, self.tile_colors[self.tiles[ring][tile].terrain], [self.tiles[ring][tile].rect_x, self.tiles[ring][tile].rect_y, self.tiles[ring][tile].rect_width, self.tiles[ring][tile].rect_height], self.tiles[ring][tile].radi_start, self.tiles[ring][tile].radi_end, self.tiles[ring][tile].ring_width)   
        
    
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

    
    def __init__(self, rect_x = 0, rect_y = 0 ,rect_height = 0, rect_width = 0, radi_start = 0, radi_end = 0,  terrain = 0, ring_width = 0, units = None):
        """
        defines the instance attributes for every tile on call
        """
        # terrain 0 = black (center), 1 = light/green, 2 normal/yellow, 3 difficult/red
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.radi_start = radi_start
        self.radi_end = radi_end
        self.terrain = terrain
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.ring_width = ring_width
        if units == None:
            self.units = []
        else:
            self.units = units
        
    def __str__(self):
        """
        string output for the class
        """
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
        
    def add_unit(self, unit):
        """
        adds a unit to the tile
        """
        pass
    
    def del_unit(self, unit):
        """
        deletes a unit from a tile
        """
        pass
        
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

        



   
        

    