# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:26:21 2019

@author: J. Tyler McGoffin
"""

from numpy.core.numeric import moveaxis
import pygame, sys
import numpy as np
from pygame import draw
from pygame.locals import *

from ship import Ship
from laser import Laser
from asteroid import Asteroid
from background import Background
from health import Health
from screw import Screw
from fuel import Fuel

# Set up window and frame rate variables
FPS = 30
WINDOWWIDTH = 500
WINDOWHEIGHT = 700

# Set up some Color variables
BLACK = (0, 0, 0)
NAVYBLUE = (0, 0, 128)
DARKPURPLE = (100, 0, 100)
WHITE = (255, 255, 255)
DARKGRAY = (100, 100, 100)



# Start the game
def main():


    global FPSCLOCK, DISPLAYSURF, BASICFONT #True globals
    
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Space Shooter")
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():
    # setup the game
    asteroidsHit = 0 # Number of asteroids destroyed
    score = 0
    lives = 3
    levelUp = False

    # Create Game Objectes: ship, asteroids, lasers, background 
   
    # Ship Controls
    playerShip = Ship(WINDOWWIDTH, WINDOWHEIGHT)
    leftHeld = False
    rightHeld = False
    upHeld = False
    downHeld = False
    firing = False
    startSpeed = 5

    # Lasers
    lasers = initializeObjects(10)
    laserIndex = 0
    laserSpeed = 10
    fireRate = 4 # lasers per second

    # Asteroid thingz
    asteroids = initializeObjects(25)
    spawnRate = 1 # on average, wel'll spawn 1 asteroid per second
    minAsteroidSpeed = 1
    maxAsteroidSpeed = 8
    asteroidIndex = 0

    # Screws
    screws = initializeObjects(6)
    screwSpawnRate = 0.08
    minScrewSpeed = 1
    maxScrewSpeed = 8
    screwIndex = 0
    
    # FuelTankBoooooost
    tanks = initializeObjects(4)
    tankSpawnRate = 0.05
    minTankSpeed = 1
    maxTankSpeed = 8
    tankIndex = 0

    #Heart
    heart_one = Health(10,30)
    heart_two = Health(40,30)
    heart_three = Health(70,30)

    # Backgrounds
    backgroundObject = Background("background", WINDOWHEIGHT)
    paralaxObject = Background("paralax", WINDOWHEIGHT)
    # game loop
    while True:
        # event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_a or event.key == K_LEFT:
                    leftHeld = True
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = True
                elif event.key == K_w or event.key == K_UP:
                    upHeld = True
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = True  
                elif event.key == K_SPACE:
                    firing = True                  
                
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_LEFT:
                    leftHeld = False
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = False
                elif event.key == K_w or event.key == K_UP:
                    upHeld = False
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = False  
                elif event.key == K_SPACE:
                    firing = False                     

        # Increase game difficulty

        if asteroidsHit % 10 == 0 and levelUp:
            minAsteroidSpeed += 2
            maxAsteroidSpeed += 2
            minScrewSpeed += 2
            maxScrewSpeed += 2
            minTankSpeed += 2
            maxTankSpeed += 2
            spawnRate += 1
            levelUp = False
        elif asteroidsHit % 10 != 0:
            levelUp = True


        # spawn lasers
        if firing: 
            lasers[laserIndex] = Laser(playerShip.rect,laserSpeed)
            firing = False
            laserIndex += 1
            if laserIndex >= len(lasers):
                laserIndex = 0


        # automate asteroid spawning
        if  np.random.randint(0, FPS/spawnRate) == 0:
            asteroids[asteroidIndex] = Asteroid(WINDOWWIDTH, WINDOWHEIGHT, np.random.randint(minAsteroidSpeed,maxAsteroidSpeed))
            asteroidIndex +=1
            if asteroidIndex >= len(asteroids):
                asteroidIndex = 0

        # spawn screw powerup
        if  np.random.randint(0, FPS/screwSpawnRate) == 0:
            screws[screwIndex] = Screw(WINDOWWIDTH, WINDOWHEIGHT, np.random.randint(minScrewSpeed,maxScrewSpeed))
            screwIndex +=1
            if screwIndex >= len(screws):
                screwIndex = 0

        # spawn tank powerup
        if  np.random.randint(0, FPS/tankSpawnRate) == 0:
            tanks[tankIndex] = Fuel(WINDOWWIDTH, WINDOWHEIGHT, np.random.randint(minTankSpeed,maxTankSpeed))
            tankIndex +=1
            if tankIndex >= len(tanks):
                tankIndex = 0

        # update state
        playerShip.move(left=leftHeld,right=rightHeld, up=upHeld, down=downHeld)
        backgroundObject.move()
        paralaxObject.move()

        for laser in lasers:
            if laser != None:
                laser.move()

        for asteroid in asteroids:
            if asteroid != None:
                asteroid.move()

        for screw in screws:
            if screw != None:
                screw.move()
        
        for tank in tanks:
            if tank != None:
                tank.move()

        for currentScrewIndex, screw in enumerate(screws):
            if screw != None:
                for currentLaserIndex, laser in enumerate(lasers):
                    if laser != None:
                        if laser.rect.colliderect(screw.rect):
                            screws[currentScrewIndex] = None
                            lasers[currentLaserIndex] = None
                            laserSpeed +=2
                            score += 100

        for currentTankIndex, tank in enumerate(tanks):
            if tank != None:
                for currentLaserIndex, laser in enumerate(lasers):
                    if laser != None:
                        if laser.rect.colliderect(tank.rect):
                            tanks[currentTankIndex] = None
                            lasers[currentLaserIndex] = None
                            startSpeed += 1
                            score += 200
                            playerShip.setStartSpeed(startSpeed)

        # detect collisions
        for currentAsteroidIndex, asteroid in enumerate(asteroids):
            if asteroid != None:
                for currentLaserIndex, laser in enumerate(lasers):
                    if laser != None:
                        if laser.rect.colliderect(asteroid.rect):
                            asteroids[currentAsteroidIndex] = None
                            lasers[currentLaserIndex] = None
                            asteroidsHit += 1
                            score += 50
                            
                if playerShip.rect.colliderect(asteroid.rect):
                    lives -= 1
                    if lives == 2:
                        heart_three.takeDamage()
                    elif lives == 1:
                        heart_two.takeDamage()
                    elif lives == 0:
                        heart_one.takeDamage()
                    if lives > 0:
                        playerHit() # write the reset code here
                        playerShip.setStartPos()
                        asteroids = initializeObjects(25)
                        lasers = initializeObjects(10)
                    else:
                        return
                    break

        # draw on screen
        DISPLAYSURF.fill(BLACK)
        draw(backgroundObject.image, backgroundObject.rect)
        draw(paralaxObject.image, paralaxObject.rect)
        drawLaser(lasers)
        drawAsteroids(asteroids)
        drawScrews(screws)
        drawTank(tanks)
        draw(imageSurf = playerShip.image, imageRect = playerShip.rect) 
        draw(heart_one.image,heart_one.rect)
        draw(heart_two.image,heart_two.rect)
        draw(heart_three.image,heart_three.rect)
        
        
        drawHUD(lives,asteroidsHit,score)

        pygame.display.update()
        FPSCLOCK.tick(FPS)    

def drawHUD(lives,asteroidsHit,totalScore):
    healthBarSurf = BASICFONT.render("Ships remaining: " +str(lives),True, WHITE)
    healthBarRect = healthBarSurf.get_rect()
    healthBarRect.topleft = (10,10)
    draw(healthBarSurf, healthBarRect)

    asteroidsHitSurf = BASICFONT.render("Asteroids destroyed: "+str(asteroidsHit), True,WHITE)
    asteroidsHitRect = asteroidsHitSurf.get_rect()
    asteroidsHitRect.topright = (WINDOWWIDTH-10,10)
    draw(asteroidsHitSurf,asteroidsHitRect)

    scoreSurf = BASICFONT.render("Total Score: " +str(totalScore),True,WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = ((WINDOWWIDTH/2) - 20, 40)
    draw(scoreSurf,scoreRect)
    
def playerHit():
    hitSurf = BASICFONT.render("You've been destroyed!", True, WHITE)
    hitRect = hitSurf.get_rect()
    hitRect.center = ((WINDOWWIDTH/2), WINDOWHEIGHT/2)
    draw(hitSurf,hitRect)
   
    pygame.display.update()
    pygame.time.wait(2000)

def drawTank(tanks):
    for tank in tanks:
        if tank != None:
            image, rect = tank.draw()
            draw(image,rect)

def drawLaser(lasers):
    for laser in lasers:
        if laser != None:
            draw(laser.image,laser.rect)
    
def drawAsteroids(asteroids):
    for asteroid in asteroids:
        if asteroid != None:
            image, rect = asteroid.draw()
            draw(image,rect)

def drawScrews(screws):
    for screw in screws:
        if screw != None:
            image, rect = screw.draw()
            draw(image,rect)


def initializeObjects(number):
    objects = []
    for x in range(number):
        objects.append(None)
    return objects

def draw (imageSurf, imageRect):
    DISPLAYSURF.blit(imageSurf, imageRect)

def terminate():
    pygame.quit()
    sys.exit()

def showGameOverScreen():
    return

def showStartScreen():
    return

if __name__ == '__main__':
    main()