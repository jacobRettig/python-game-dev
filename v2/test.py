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
MASTER_SHEET = spriteSheetSimple.SpriteSheetControl()
sheet = spriteSheetSimple.SpriteSheet(MASTER_SHEET, gender='female', shoes='black', pants='skirt', hair='bedhead', eyes='green', left_hand='arrow',\
     right_hand="recurvebow")

txt = None
with open('testMap.txt', 'r') as file:
    txt = file.readlines()
world = World(txt)
camera = Camera(background, world)

#main infinite loop
def main():
    while True:
#        default event loop
        for event in pygame.event.get():
#             Quit conditions
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return
        
        
#         update calls
        
        world.update()
        
                

#         draw background
        screen.blit(background, (0, 0))
        camera.draw(screen)
#         draw calls
#         screen.blit(sheet.image, (0, 0))
#         loop ending
        pygame.display.flip()
        print(world.player.tl)
        clock.tick(TICK_SPEED)
    
#Start execution
main()
pygame.quit()
