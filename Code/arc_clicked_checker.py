# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:31:11 2016

@author: Florian Jehn
"""
import pygame
from pygame.locals import *
import sys
from math import atan2, pi

class CircularArc:

    def __init__(self, color, center, radius, start_angle, stop_angle, width=1):
        self.color = color
        self.x = center[0]  # center x position
        self.y = center[1]  # center y position
        self.rect = [self.x - radius, self.y - radius, radius*2,  radius*2]
        self.radius = radius
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = width




    def draw(self, canvas):
        pygame.draw.arc(canvas, self.color, self.rect, self.start_angle, self.stop_angle, self.width)



    def contains(self, x, y):

        dx = x - self.x   # x distance
        dy = y - self.y   # y distance

        greater_than_outside_radius = dx*dx + dy*dy >= self.radius*self.radius

        less_than_inside_radius = dx*dx + dy*dy <= (self.radius- self.width)*(self.radius- self.width)

        # Quickly check if the distance is within the right range
        if greater_than_outside_radius or less_than_inside_radius:
            return False



        rads = atan2(-dy, dx)  # Grab the angle

        # convert the angle to match up with pygame format. Negative angles don't work with pygame.draw.arc
        if rads < 0:
            rads = 2 * pi + rads


        # Check if the angle is within the arc start and stop angles
        return self.start_angle <= rads <= self.stop_angle

#
pygame.init()


black = ( 0, 0, 0)
width = 800
height = 800
screen = pygame.display.set_mode((width, height))


distance = 100
tile_num = 4
ring_width = 20

arc = CircularArc((255, 255, 255), [width/2, height/2], 100, tile_num*(2*pi/7), (tile_num*(2*pi/7))+2*pi/7, int(ring_width*0.5))

while True:

    fill_color = black

    for event in pygame.event.get():
        # quit if the quit button was pressed
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    x, y = pygame.mouse.get_pos()


    # Change color when the mouse touches
    if arc.contains(x, y):
        fill_color = (200, 0, 0)


    screen.fill(fill_color)
    arc.draw(screen)
    # screen.blit(debug, (0, 0))
    pygame.display.update()