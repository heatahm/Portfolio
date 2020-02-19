import numpy as np
import random as rn
import pygame, sys
from pygame.locals import *

x,y = 32,24
SIZE = 20

#Change these to have more or fewer blocks
#x,y = 200,300
#SIZE = 4

a = np. zeros ((x,y),dtype = list)

for i in range(0,x):
    for j in range(0,y):
        a[i][j] = [rn.randint(0,1),rn.randint(0,1)]

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
PINK      = (255, 105, 180)
RED       = (255,   0,   0)
ORANGE    = (255,  51,   0)
YELLOW    = (255, 255,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
PURPLE    = (128,   0, 128)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640, 480))
#Ends
def terminate():
    pygame.quit()
    sys.exit()
#Draws cell at loc using color
def draw_at(loc,color):
    x,y = loc
    x = x*SIZE
    y = y*SIZE
    pygame.draw.rect(DISPLAYSURF, color,((x+1,y),(SIZE-1,SIZE-1)))

############################################################
def countLiveNeighbors(i,j):
    rows = [i-1,i,i+1]
    cols = [j-1,j,j+1]
    neighbors = []
    for m in rows:
        if m >= 0 and m < len(a):
            for n in cols:
                if n >= 0 and n < len(a[0]):
                    if not (n == j and m == i):
                        neighbors.append((m,n))
    friends = 0
    for k in neighbors:
        friends += a[k[0]][k[1]][0]

    return friends   

#Generates 0,1 depending on rules
#needs fixing
def next(i,j):
    n = countLiveNeighbors(i,j)
    if a[i][j][0] == 1:
        if (n < 2):
            return 0
        elif n > 3:
            return 0
        else:
            return 1
    else:
        if n == 3:
            return 1
        else: 
            return 0
        
############################################################
#Shifts the Boolean values in the list forward
def shift():
    for i in range(0,x):
        for j in range(0,y):
            a[i][j] = [a[i][j][0], next(i,j)]
    for i in range(0,x):
        for j in range(0,y):
            a[i][j] = [a[i][j][1], 0]
            
#assigns a color for the cell
def getColor(loc):
    ##Comment and uncomment to get fun color combinations!

    #return (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255))
    
    n = int(x/6)

    if loc[0] < n:
        return RED
    elif loc[0] < 2*n:
        return ORANGE
    elif loc[0] < 3*n:
        return YELLOW
    elif loc[0] < 4*n:
        return GREEN
    elif loc[0] < 5*n:
        return BLUE
    else:
        return PURPLE
    """
    if loc[0] < 255 and loc[1] < 255:
        return (loc[0],loc[1],100)
    else:
        return (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255))
    """

#Draws all the cells that have [1,x] 
def draw_all():
    for i in range(0,x):
        for j in range(0,y):
            if a[i][j][0] == 1:
                draw_at((i,j),(getColor((i,j))))

myclock = pygame.time.Clock()    

while True:

    for event in pygame.event.get(): 
        if event.type == QUIT:
            terminate()
        else:
            pygame.event.clear()
            DISPLAYSURF.fill(BGCOLOR)
            draw_all()
            pygame.display.update()
            pygame.event.clear()
            myclock.tick(40)
            shift()

