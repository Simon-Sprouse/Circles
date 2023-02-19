#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:37:17 2023

@author: simonsprouse
"""

import pygame as pg
import random 
import math



class Snake():
    
    def __init__(self, surface):
        self.surface = surface
        self.pos = (200,200)
        self.show = False
        self.color = (0,0,0)
        self.radius = 10
        self.border_color = (255,255,255)
        self.border_size = 2
        
    def findPos(self):
        
        dr = random.randint(0,20)
        theta = random.randint(0,359)
        
        dx = dr * math.cos(theta)
        dy = dr * math.sin(theta)
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)
        

        
    def drawCircle(self): 
        
        pg.draw.circle(self.surface, self.border_color, 
                       self.pos, self.radius + self.border_size)
        pg.draw.circle(self.surface, self.color, 
                       self.pos, self.radius)
        
        
    def go(self): 
        self.show = not self.show
        
    def run(self):
        
        if self.show == True:
        
            self.findPos()
            self.drawCircle()
        
        