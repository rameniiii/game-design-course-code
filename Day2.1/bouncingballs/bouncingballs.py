import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

WINDOWHEIGHT = 600
WINDOWWIDTH = 800

xVelocity = 6 
yVelocity = 6

radius = 40

centerOfBallX = 200
centerOfBallY = 200




while True:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLUE, (centerOfBallX, centerOfBallY), 40,)

    centerOfBallX += xVelocity 
    centerOfBallY += yVelocity


    if centerOfBallX < radius or centerOfBallX >= WINDOWWIDTH:
	    xVelocity *= -1
    elif centerOfBallY < radius or centerOfBallY >= WINDOWHEIGHT:
        yVelocity *= -1
    



    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
