#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:28:56 2023

@author: simonsprouse
"""

import pygame as pg
from Snake import Snake


pg.init()


window_height = 500
window_length = 500
window_size = (500,500)
tan = (255,244,193)

window = pg.display.set_mode((window_size), pg.RESIZABLE)
pg.display.set_caption("Funky Circle Time")
window.fill(tan)





snake1 = Snake(window)



running = True

while running == True:
    
    pg.display.flip()
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            
            running = False
            
        if event.type == pg.MOUSEBUTTONDOWN:
            
            
            snake1.run()
            snake1.find_pos()
            
            
            
            
pg.quit()