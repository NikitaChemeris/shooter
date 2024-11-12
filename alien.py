import pygame
from random import randint, choice
from constants import SCREEN_WIDTH, ALIEN_STEP
from pathlib import Path


class Alien:
    def __init__(self):
        self.image = self.alien_image()
        self.width, self.height = self.image.get_size()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.step = ALIEN_STEP
        self.speed = self.step

    @staticmethod
    def alien_image():
        images = [img for img in Path('images/aliens').iterdir() if img.suffix.lower() == '.png']
        return pygame.image.load(str(choice(list(images)))).convert_alpha()

    def update_position(self):
        self.y += self.speed

    def increase_speed(self):
        self.speed += self.step / 2

    def reset(self):
        self.increase_speed()
        self.image = self.alien_image()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0


    def has_reached_fighter(self, fighter):
        return self.y + self.height > fighter.y



