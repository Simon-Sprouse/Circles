#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:28:56 2023

@author: simonsprouse
"""

import pygame as pg


pg.init()


window_height = 500
window_length = 500
window_size = (500,500)
tan = (255,244,193)




window = pg.display.set_mode((window_size), pg.RESIZABLE)

pg.display.set_caption("Funky Circle Time")
    
window.fill(tan)

pg.display.flip()







running = True

while running == True:
    
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            
            running = False
            
            
            
            
pg.quit()