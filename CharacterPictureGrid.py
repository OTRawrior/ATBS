# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:12:59 2018

@author: Reece
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotateGrid(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print((grid[x][y]), end='')
        print('')
        
        
rotateGrid(grid)