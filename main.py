import pygame
import sys

pygame.init()


pygame.display.set_mode((800, 600))

pygame.display.set_caption("My Pygame")

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()