import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Background:
    def __init__(self):
        self.image = pygame.image.load('images/bc.png').convert()
        self.transfer_size()

    def transfer_size(self):
        self.image = pygame.transform.flip(self.image, SCREEN_WIDTH, SCREEN_HEIGHT)


