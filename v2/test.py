'''
Created on May 4, 2015

@author: jacobrettig
'''

import cProfile

import pygame

from camera import Camera
from world import World


#Settings for GUI
WIDTH, HEIGHT = 700, 700
TICK_SPEED = 30
BACKGROUND_COLOR = (255, 255, 255)

#Initialize GUI stuff
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size()).convert()
background.fill(BACKGROUND_COLOR)

#Recycle GUI Settings names
del WIDTH
del HEIGHT

#Useful Functions
def isShiftDown():
    return pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]


#Initialize variables
txt = None
with open('testMap.txt', 'r') as file:
    txt = file.readlines()
world = World(txt)
world.player.speed = 4
world.player.animation['beard'] = 'mustache'

for i in range(5):
    world.addEnemy()
    
    
camera = Camera(background, world, 1)

profile = cProfile.Profile()
profile.enable()


#main infinite loop
def main():
#        default event loop
    for event in pygame.event.get():
#             Quit conditions
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return False
    
    
#         update calls
    
    world.update()
    
    camera.draw(screen)
    pygame.display.flip()
    
    clock.tick(TICK_SPEED)
    return True
    
#Start execution
while main():
    pass

profile.disable()
profile.print_stats(2)


pygame.quit()
