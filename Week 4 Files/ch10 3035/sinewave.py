import pygame, sys
from pygame.locals import *

# math module needed for trig functions
import math

pygame.init()

# setup the window
DISPLAYSURF = pygame.display.set_mode((720,200),0,32)
pygame.display.set_caption('Sine Wave: (yellow), cosine wave: (red). 0 to 720 degrees')

#setup the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

#draw on the surface
DISPLAYSURF.fill(BLACK)

# draw a baseline
pygame.draw.line(DISPLAYSURF,GREEN,(0,100),(720,100),1)


# loop from 0 to 720 degrees in steps of 3 degrees
for degrees in range(0,721,3):
            
    # convert degrees to radians, find sine and cosine
    sin_value = math.sin(math.radians(degrees))
    cos_value = math.cos(math.radians(degrees))

    # calculate y coordinate for sine and cosine
    sin_ycoord = 100 - int(100 * sin_value)
    cos_ycoord = 100 - int(100 * cos_value)

    # draw sine wav
    pygame.draw.circle(DISPLAYSURF, YELLOW, (degrees,sin_ycoord),2,2)

    # draw cosine wav
    pygame.draw.circle(DISPLAYSURF, RED, (degrees,cos_ycoord),2,2)
    

# run the game loop                    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

     
