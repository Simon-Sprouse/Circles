#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:37:17 2023

@author: simonsprouse
"""

import pygame as pg

def drawCircle(surface, color, position, radius): 
    
    pg.draw.circle(surface, color, position, radius)
    

class Snake():
    
    def __init__(self, surface):
        self.surface = surface
        self.pos = (0,0)
        self.show = True
        
    def run(self):
        pos = pg.mouse.get_pos()
        drawCircle(self.surface, (0,0,0), pos, 10)
        