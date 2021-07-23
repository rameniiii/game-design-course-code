import random,pygame,sys
from pygame.display import set_gamma
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window width must be a multiple of cell size"
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

# Define Colors
# Name (R,B,B)
WHITE = (255,255,255)
BLACK = (0,0,0,)
RED = (255,0,0)
GREEN = (0,255,0)
DARKGREEN = (0, 155,0)
DARKGRAY = (40,40,40)
BLUE = (0,0,255)
BGCOLOR = BLACK
PINK = (230,0,126)

# KEY INPUT = worm direction
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # The index of the worm's head
HEADTWO = 0
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, TIMER

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('Wormy')

    
    showStartScreen()

    while True:
        runGame()
        showGameOverScreen()

def runGame():

    #Spawn at a random starting point
    startx = random.randint(5,CELLWIDTH - 6)
    starty = random.randint(5,CELLHEIGHT - 6)

    startx_two = random.randint(2,CELLWIDTH - 5)
    starty_two = random.randint(2,CELLHEIGHT - 5)

    direction = RIGHT # CALLOUT
    direction_two = RIGHT
    wormCoords =   [{'x': startx,    'y': starty},
                    {'x': startx -1, 'y':starty-1},
                    {'x': startx-2,  'y': starty-1}]

    wormCoords_two = [{'x': startx_two ,  'y': starty_two},
                    {'x': startx_two , 'y':starty_two},
                    {'x': startx_two,  'y': starty_two}]

    apple = getRandomLocation()
    apple_two = getRandomLocation()


    # Game loop (while)

    direction = RIGHT
    direction_two = RIGHT
    while True:
        

        
    # Event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                pygame.time.set_timer(event,0)
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction_two = LEFT
                elif (event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT) and direction != LEFT:
                    direction_two = RIGHT
                elif (event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP) and direction != DOWN:
                    direction_two = UP
                elif (event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN) and direction != UP:
                    direction_two = DOWN
                elif (event.key == K_s) and direction != UP:
                    direction = DOWN

                elif event.key == K_ESCAPE:
                    terminate()


        # Detect "collisions"
        # check to see if the worm has hit itself or the wall
        



        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return
        
        for wormSegment in wormCoords[3:]:
            if wormSegment['x'] == wormCoords[HEAD]['x'] and wormSegment['y'] == wormCoords[HEAD]['y']:
                return


        if wormCoords_two[HEADTWO]['x'] == -1 or wormCoords_two[HEADTWO]['y'] == -1 or wormCoords_two[HEADTWO]['x'] == CELLWIDTH or wormCoords_two[HEADTWO]['y'] == CELLHEIGHT:
            return

        for wormSegment_two in wormCoords_two[3:]:
            if wormSegment_two['x'] == wormCoords_two[HEADTWO]['x'] and wormSegment_two['y'] == wormCoords_two[HEADTWO]['y']:
                return

        # check to see if the worm has eaten the apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()
        else: del wormCoords[-1]
        
        if wormCoords_two[HEAD]['x'] == apple_two['x'] and wormCoords_two[HEADTWO]['y'] == apple_two['y']:
            apple_two = getRandomLocation()
        else: del wormCoords_two[-1]

        #move the worm

        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y' : wormCoords[HEAD]['y'] -1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y' : wormCoords[HEAD]['y'] +1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y' : wormCoords[HEAD]['y'] }
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y' : wormCoords[HEAD]['y'] }


        if direction_two == UP:
            newHeadTwo = {'x': wormCoords_two[HEADTWO]['x'], 'y' : wormCoords_two[HEADTWO]['y'] -1}
        elif direction_two == DOWN:
            newHeadTwo = {'x': wormCoords_two[HEADTWO]['x'], 'y' : wormCoords_two[HEADTWO]['y'] +1}
        elif direction_two == LEFT:
            newHeadTwo = {'x': wormCoords_two[HEADTWO]['x'] - 1, 'y' : wormCoords_two[HEADTWO]['y'] }
        elif direction_two == RIGHT:
            newHeadTwo = {'x': wormCoords_two[HEADTWO]['x'] + 1, 'y' : wormCoords_two[HEADTWO]['y'] }
        
        wormCoords.insert(0, newHead)
        wormCoords_two.insert(0,newHeadTwo)
        
       


        # LAST THING WE DO           
        # Paint on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawWorm_two(wormCoords_two)
        drawApple(apple)
        drawApple_two(apple_two)
        drawScore(len(wormCoords)-3)
        drawScore_two(len(wormCoords_two)-3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getRandomLocation():
    return {'x':random.randint(2,CELLWIDTH -2), 'y': random.randint(2,CELLHEIGHT -2)}

def drawGrid():
    for x in range (0,WINDOWWIDTH,CELLSIZE):
        pygame.draw.line(DISPLAYSURF,DARKGRAY,(x,0), (x,WINDOWHEIGHT))
    for y in range (0,WINDOWWIDTH,CELLSIZE):
        pygame.draw.line(DISPLAYSURF,DARKGRAY,(0,y), (WINDOWHEIGHT,y))
                

def drawWorm(wormCoords):
    for segment in wormCoords:
        x = segment['x'] * CELLSIZE
        y = segment['y'] * CELLSIZE

        wormSegmentRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
        pygame.draw.rect(DISPLAYSURF,BLUE,wormSegmentRect)

        wormInnerSegmentRect = pygame.Rect(x+4,y+4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect)
    
def drawWorm_two(wormCoords_two):

     for segment2 in wormCoords_two:
        x_2 = segment2['x'] * CELLSIZE
        y_2 = segment2['y'] * CELLSIZE

        wormSegmentRect_two = pygame.Rect(x_2,y_2,CELLHEIGHT,CELLHEIGHT)
        pygame.draw.rect(DISPLAYSURF,GREEN,wormSegmentRect_two)

        wormInnerSegmentRect_two = pygame.Rect(x_2+4,y_2+4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect_two)


def drawApple(apple):
    x = apple['x'] * CELLSIZE
    y = apple['y'] * CELLSIZE
    appleSegmentRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleSegmentRect)
    return

def drawApple_two(apple_two):
    x_2 = apple_two['x'] * CELLSIZE
    y_2 = apple_two['y'] * CELLSIZE
    appleSegmentRect = pygame.Rect(x_2,y_2,CELLSIZE,CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, PINK, appleSegmentRect)
    return

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    return
    
def drawScore_two(score_two):
    scoreSurf = BASICFONT.render('Score: %s' % (score_two), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (10, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    return

def terminate():
    pygame.quit()
    sys.exit()
    
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2,10)
    overRect.midtop = (WINDOWWIDTH/2,gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf,gameRect)
    DISPLAYSURF.blit (overSurf,overRect)

    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear the event cache


    while True:
        if checkForKeyPress():
            pygame.event.get()
            return

def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            else: 
                return True
    return
def showStartScreen():
    return

if __name__ == '__main__':
    main()