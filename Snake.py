#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:37:17 2023

@author: simonsprouse
"""

import pygame as pg
import random 
import math

def drawCircle(surface, color, position, radius): 
    
    pg.draw.circle(surface, color, position, radius)
    


    

class Snake():
    
    def __init__(self, surface):
        self.surface = surface
        self.pos = (200,200)
        self.show =True
        self.color = (0,0,0)
        
    def find_pos(self):
        
        dr = random.randint(0,20)
        theta = random.randint(0,359)
        
        dx = dr * math.cos(theta)
        dy = dr * math.sin(theta)
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)
        
        # print(self.pos)
        
        
    def run(self):
        drawCircle(self.surface, self.color, self.pos, 10)
        
        