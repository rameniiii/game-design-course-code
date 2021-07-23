import pygame

class FullHeart:

    def __init__(self, WINDOWWIDTH, WINDOWHEIGHT):
        self.image = pygame.transform.scale(pygame.image.load("ArtAssets7/pixelheart.pn"),(40,40))
        self.rect = self.image.get_rect()