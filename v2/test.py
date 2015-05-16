'''
Created on May 4, 2015

@author: jacobrettig
'''

import pygame

import spriteSheetSimple
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


for i in range(4):
    world.addEnemy()
    
    
camera = Camera(background, world)

import cProfile
profile = cProfile.Profile()
profile.enable()


#main infinite loop
def main():
#     while True:
#        default event loop
    for event in pygame.event.get():
#             Quit conditions
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return
    
    
#         update calls
    
    world.update()

    camera.draw(screen)
    pygame.display.flip()
    
    clock.tick(TICK_SPEED)
    
#Start execution
for i in range(100):
    main()

profile.disable()
profile.print_stats(2)


pygame.quit()
