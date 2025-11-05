import pygame
from random import randint
from width_height import *

def make_background():
    background_file = 'kenney_space-shooter-redux/Backgrounds/darkPurple.png' #gives path in files
    background_load = pygame.image.load(background_file) #simplifies the process of loading tiles, by using a var

    tile_width = background_load.get_width()
    tile_height = background_load.get_height()

    background = pygame.Surface((WIDTH,HEIGHT))

    # loop over the background and place tiles on it
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(background_load, (x,y))

    brown_meteors_file = 'kenney_space-shooter-redux/PNG/Meteors/meteorBrown_big3.png' 
    brown_meteors_load = pygame.image.load(brown_meteors_file)

    grey_meteors_file = 'kenney_space-shooter-redux/PNG/Meteors/meteorGrey_med2.png'
    grey_meteors_load = pygame.image.load(grey_meteors_file)

    purple_planet_file = 'kenney_planets/Planets/planet09.png'
    purple_planet_load = pygame.image.load(purple_planet_file)

    blue_green_planet = 'kenney_planets/Planets/planet03.png'
    blue_green_planet_load = pygame.image.load(blue_green_planet)



    return background