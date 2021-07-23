import pygame

class Health():

    def __init__(self, xPos, yPos):
        self.image = pygame.transform.scale(pygame.image.load("ArtAssets7/pixelheart.png"),(40,40))
        self.rect = self.image.get_rect()
        self.xPos = xPos
        self.yPos = yPos
        self.transparent = (0,0,0,0)

        self.setPos()


    def setPos(self):
        self.rect.topleft = (self.xPos,self.yPos)

    def takeDamage(self):
        self.image.fill(self.transparent)
    
