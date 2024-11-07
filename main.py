import pygame
import sys

pygame.init()

screen_with, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_with, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_with / 2 - fighter_width / 2, screen_height - fighter_height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    pygame.display.update()