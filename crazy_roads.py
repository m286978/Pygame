import pygame
from random import randint
from width_height import *
from game_background import make_background

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starry Night")
clock = pygame.time.Clock()
running = True

background = make_background()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # pass the event to our player
        background.blit(background_load, (x,y))

    
    pygame.display.flip()

    clock.tick(60)
  # limits FPS to 60

pygame.quit()