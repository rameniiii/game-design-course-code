import pygame, sys
from pygame.locals import *
import math

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

WINDOWHEIGHT = 600
WINDOWWIDTH = 800

ballone_xVelocity = 6
ballone_yVelocity = 6

balltwo_xVelocity = 8
balltwo_yVelocity = 8



ball_one_radius = 40
ball_two_radius = 40

ballone_xCenter = 200
ballone_yCenter = 200

balltwo_xCenter = 400
balltwo_yCenter = 400

ballone_point = [ballone_xCenter,ballone_yCenter]
balltwo_point = [balltwo_xCenter,balltwo_yCenter]






distance_between_centers = 0


def detectCollision(ballone_point, balltwo_point):
    distance_between_centers = math.sqrt(math.pow((balltwo_point[0]-ballone_point[0]),2) + (math.pow((balltwo_point[1] - ballone_point[1]),2)) * 1.0)
    if (distance_between_centers < (ball_one_radius + ball_two_radius)):
        return True
    else:
        return False


def calculate_ballone_new_velocity(ballone_point, balltwo_point):
    scale_factor = (2 * (ballone_xVelocity * (ballone_point[0] - balltwo_point[0]) + ballone_yVelocity * (ballone_point[1] - balltwo_point[1]))) / ((math.pow((ballone_point[0] - balltwo_point[0]),2))+(math.pow((ballone_point[1] - balltwo_point[1]),2)))
    new_ballone_xVelocity = ballone_xVelocity - (scale_factor * (ballone_point[0] - balltwo_point[0]))
    new_ballone_yVelocity = ballone_yVelocity - (scale_factor * (ballone_point[1] - balltwo_point[1]))
    #new_ballone_Velocity = math.sqrt(math.pow(new_ballone_xVelocity,2) + math.pow(new_ballone_yVelocity,2))
    
    return (int(new_ballone_xVelocity), int(new_ballone_yVelocity))

def calculate_balltwo_new_velocity(ballone_point, balltwo_point):
    scale_factor_two = (2 * (balltwo_xVelocity * (balltwo_point[0] - ballone_point[0]) + (ballone_yVelocity * (balltwo_point[1] - ballone_point[1])))) / ((math.pow((ballone_point[0] - balltwo_point[0]),2))+(math.pow((ballone_point[1] - balltwo_point[1]),2)))
    new_balltwo_xVelocity = balltwo_xVelocity - (scale_factor_two * (balltwo_point[0] - ballone_point[0]))
    new_balltwo_yVelocity = balltwo_yVelocity - (scale_factor_two * (balltwo_point[1] - ballone_point[1]))
    #new_balltwo_Velocity = math.sqrt(math.pow(new_balltwo_xVelocity,2) + math.pow(new_balltwo_yVelocity,2))
    return (int(new_balltwo_xVelocity), int(-1 * new_balltwo_yVelocity))   


   


while True:

    
   

    # python3 twobouncingballs.py
   
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLUE, (ballone_xCenter, ballone_yCenter), ball_one_radius,)
    pygame.draw.circle(DISPLAYSURF, RED, (balltwo_xCenter, balltwo_yCenter), ball_two_radius,)



    ballone_xCenter += ballone_xVelocity
    ballone_point.insert(0,ballone_xCenter)
    ballone_yCenter += ballone_yVelocity
    ballone_point.insert(1,ballone_yCenter)

    balltwo_xCenter += balltwo_xVelocity
    balltwo_point.insert(0,balltwo_xCenter)
    balltwo_yCenter += balltwo_yVelocity
    balltwo_point.insert(1,balltwo_yCenter)

    if ballone_xCenter < ball_one_radius or ballone_xCenter >= WINDOWWIDTH - ball_one_radius:
	    ballone_xVelocity *= -1
    elif ballone_yCenter < ball_one_radius or ballone_yCenter >= WINDOWHEIGHT - ball_two_radius:
        ballone_yVelocity *= -1
    

    if balltwo_xCenter < ball_two_radius or balltwo_xCenter >= WINDOWWIDTH - ball_two_radius:
	    balltwo_xVelocity *= -1
    elif balltwo_yCenter < ball_two_radius or balltwo_yCenter >= WINDOWHEIGHT - ball_two_radius:
        balltwo_yVelocity *= -1

    if detectCollision(ballone_point,balltwo_point) == True:
        ballone_xVelocity,ballone_yVelocity = calculate_ballone_new_velocity(ballone_point, balltwo_point)
        balltwo_xVelocity,balltwo_yVelocity = calculate_balltwo_new_velocity(balltwo_point, ballone_point)

    


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
