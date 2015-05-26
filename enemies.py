'''
Created on May 20, 2015

@author: jacobrettig
'''



import cProfile
import random
import sys

import pygame
import pygame

import engine
from engine.action import Action
from engine.camera import Camera
from engine.world import World


# @engine.action.Action('hurt')
# def death(self, owner):
#     owner.hp = 9999
#     owner.animation.speed = 9
# @death.setTrigger
# def death(self, owner):
#     return owner.hp <= 0
# @death.setOnCycle
# def death(self, owner):
#     owner.isAlive = False
    
    
# @engine.action.Action('slash')
    


# class Enemy(engine.enemy.Enemy):
#     levels = (
#         frozenset((
#             ('speed', (2, 2.5, 2.75)),
#             ('hp', (17, 18, 18.5)),
#             ('strength', (1, 1.5, 2)),
#             ('action1', ()),
#             ('gender', ('male', 'female')),
#             ('body', ('orc',))
#             ))
#         )
#     
#     def __init__(self, world, level):
#         self.level = level
#         engine.enemy.Enemy.__init__(self, world)
#         self.randomizeAttributes(50)
#         self.acts = [death]
#         
#     def randomizeAttributes(self, tries):
#         for option in self.levels[self.level]:
#             lst = list(option[1])
#             option = option[0]
#             while True:
#                 try:
#                     selection = lst.pop(random.randint(0, len(lst) - 1)) 
#                     if option in engine.spriteSheetLPC.LPC.TAG_CATEGORIES:
#                         self[option] = selection
#                     elif option == 'speed':
#                         self.speed = selection
#                     elif option == 'hp':
#                         self.hp = selection
#                     elif option == 'strength':
#                         self.strength = selection
#                     elif option in ('action1', 'action2'):
#                         self.acts.append(selection)
#                     else:
#                         print('failed to find : {}'.format(selection))
#                         sys.exit()
#                 except Exception as err:
#                     if len(lst) == 0:
#                         raise err
#                 else:
#                     break


class EnemyD(engine.enemy.Enemy):
    def __init__(self, world, level):
        self.level = level
        engine.enemy.Enemy.__init__(self, world)
        self.cen = world.map.openTiles[random.randint(0, len(world.map.openTiles) - 1)].cen()
        self['nose'] = 'none'
        self['ears'] = 'none'
        self['eyes'] = 'none'
        self['body'] = 'red_orc'
        self['pants'] = 'skirt'
        self['shoes'] = 'none'
        self['shirt'] = 'none'
        self['hair'] = 'none'
        self['right hand'] = 'dagger'
        
        if level > 1:
            self['body'] = 'red_orc'
        
        
        
'''
Created on May 19, 2015

@author: lisarettig
'''
'''
Created on May 4, 2015

@author: jacobrettig
'''





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



@Action('slash')
def attackPlayer(self, owner):
    owner.isMoving = False
    owner.animation.speed = 8
    self.counter += 1
    for entity in world.entityList:
        if owner != entity and owner.cen.gethypot(entity.cen) <= owner.visDistance:
            entity.hp -= 5
attackPlayer.counter = 0
@attackPlayer.setTrigger
def attackPlayer(self, owner):
    return pygame.key.get_pressed()[pygame.K_SPACE]
    for entity in world.entityList:
        if owner != entity and owner.cen.gethypot(entity.cen) <= owner.visDistance:
            return True
        
@Action('slash')
def attackEnemy(self, owner):
    owner.isMoving = False
    if owner.world.player in owner.seen and owner.world.player.cen.gethypot(owner.cen) <= owner.hearDistance:
        owner.world.player.hp -= 2
@attackEnemy.setTrigger
def attackEnemy(self, owner):
    return owner.world.player in owner.seen and owner.world.player.cen.gethypot(owner.cen) <= owner.hearDistance
    
@Action('hurt')
def death(self, owner):
    print('died')
    owner.animation.speed = 10
    owner.isMoving = False
    owner.hp = 99999
@death.setOnCycle
def death(self, owner):
    owner.isAlive = False
@death.setTrigger
def death(self, owner):
    print('death trigger')
    return owner.hp <= 0
#     owner.hp = 20
#     import random
#     owner.cen = world.map.openTiles[random.randint(0, len(world.map.openTiles) - 1)].cen()
#     owner.target = owner.cen()
#     owner.action = -1
@death.setTrigger
def death(self, owner):
    return owner.hp <= 0
    
def addEnemy():
    E = EnemyD(world, 3)
    E.target = E.cen()
    
    
    world.entityList.add(E)



#Initialize variables
txt = None
with open('engine/testMap.txt', 'r') as file:
    txt = file.readlines()
world = World(txt)
world.player.speed = 4
world.player.acts = [attackPlayer, death]
world.player['beard'] = 'mustache'
world.player['right hand'] = 'spear'
world.player['left hand'] = 'arrow'

for i in range(12):
    addEnemy()
    
    
camera = Camera(background, world, 1)

# profile = cProfile.Profile()
# profile.enable()


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

# profile.disable()
# profile.print_stats(2)


pygame.quit()

        
        
        
        
        
        
        