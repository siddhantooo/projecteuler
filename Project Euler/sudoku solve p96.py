# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 12:27:51 2017

@author: Siddhant
"""

import numpy as np
import pandas as pd
import time
import itertools as it

start = time.time()

def sudoku_solve(rows):
    #input is list of rows.
    #first create columns and boxes.
    empty_set = set()
    rows = [list(row) for row in rows]
    columns = dict((j,empty_set) for j in range(9))    
    for row in rows:
        for j in range(9):
            columns[j]= columns[j].union(row[j])
            columns[j]= columns[j].difference('0')
    boxes = dict((j,set(rows[3*(j[0])][3*(j[1]):3*(j[1])+3])) for j in it.product(range(3),repeat=2))
    for j in it.product(range(3),repeat=2):
        boxes[j] = boxes[j].union(rows[3*(j[0])+1][3*(j[1]):3*(j[1])+3])
        boxes[j] = boxes[j].union(rows[3*(j[0])+2][3*(j[1]):3*(j[1])+3]).difference('0')
    
    ### actual solving
    
    count = 0
    done = 0 
    changes_made = 0
    while not done:
        count += 1
        zero_count = 0
    #    print(count)
        changes_made_in_iter = 0
        possible = dict(((r,c),set()) for (r,c) in it.product(range(9),repeat=2))
        for r in range(9):
            possible[r] = set("123456789")
            for c in range(9):
    #            print(r,c,rows[r][c])
    #            input()
                if not int(rows[r][c]):
                    zero_count += 1
                    possible[(r,c)] = set("123456789").difference(set(rows[r]).union(columns[c]).union(boxes[(r//3,c//3)]))
#                    print(r,c,possible,set(rows[r]),columns[c],boxes[(r//3,c//3)])                    
#                    input()
                    if len(possible) == 1:
                        columns[c] = columns[c].union(possible)
                        boxes[(r//3,c//3)] = boxes[(r//3,c//3)].union(possible)
                        for p in possible:
                            rows[r][c] = p
                        changes_made += 1
                        changes_made_in_iter += 1
    #                    print(r,c,possible,rows[r],columns[c])                
    #                    input()
            
        if not zero_count:
            done = 1
            break
        if not changes_made_in_iter:
            for r in range(9):
                if i not in rows[r]:
                    count_i = 0
                    for c in 
    return done, rows, count

grid = """040000050
001943600
009000300
600050002
103000506
800020007
005000200
002436700
030000040"""
rows = grid.splitlines()
    
print(sudoku_solve(rows))

print("It took the program", time.time()-start,"seconds to complete.")
