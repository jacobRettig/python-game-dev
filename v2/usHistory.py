'''
Created on May 19, 2015

@author: lisarettig
'''
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

from action import Action
import pygame



@Action('slash')
def attackPlayer(self, owner):
    owner.isMoving = False
    owner.animation.speed = 8
    self.counter += 1
    for entity in world.entityList:
        if owner != entity and owner.cen.gethypot(entity.cen) <= 500:
            print(self.counter, entity.hp)
            entity.hp -= 5
attackPlayer.counter = 0
@attackPlayer.setTrigger
def attackPlayer(self, owner):
    return pygame.key.get_pressed()[pygame.K_SPACE]
    for entity in world.entityList:
        if owner != entity and owner.cen.gethypot(entity.cen) <= 500:
            return True
        
@Action('slash')
def attackEnemy(self, owner):
    owner.isMoving = False
    if owner.world.player.cen.gethypot(owner.cen) <= 500:
        owner.world.player.hp -= 2
@attackEnemy.setTrigger
def attackEnemy(self, owner):
    return owner.world.player.cen.gethypot(owner.cen) <= 500
    
@Action('hurt')
def death(self, owner):
    owner.animation.speed = 10
    owner.isMoving = False
    owner.hp = 99999
@death.setOnCycle
def death(self, owner):
    owner.hp = 20
    import random
    owner.cen = world.map.openTiles[random.randint(0, len(world.map.openTiles) - 1)].cen()
    owner.target = owner.cen()
    owner.action = -1
@death.setTrigger
def death(self, owner):
    return owner.hp <= 0
    
def addEnemy():
    from enemy import Enemy
    E = Enemy(world, (0, 0, World.SIZE/2))
    E['eyes'] = 'none'
    E['ears'] = 'none'
    E['nose'] = 'none'
    E['beard'] = 'none'
    E['hair'] = 'none'
    E['body'] = 'skeleton'
    E['shirt'] = 'none'
    E['shoes'] = 'none'
    E['pants'] = 'none'
    E['right hand'] = 'dagger'
    E.acts = [attackEnemy, death]
    E.speed = 1.5
    
    blurbs = (
            'Hitler\'s been elected Chancellor! WWII D:', 
            'I\'m sooo hungry and unemployed!',
            'My crops are gone!',
            'It\'s hard to get foreign goods now!',
            'My money is gone from the bank! ', 
            'I want out of Hooverville!',
            'The U.S. ' 
              )
    import random
    E.blurbs['text'].append(blurbs[random.randint(0, len(blurbs) - 1)])
    
    import random
    
    E.cen = world.map.openTiles[random.randint(0, len(world.map.openTiles) - 1)].cen()
    
    E.target = E.cen()
    world.entityList.add(E)



#Initialize variables
txt = None
with open('testMap.txt', 'r') as file:
    txt = file.readlines()
world = World(txt)
world.player.speed = 4
world.player.acts = [attackPlayer, death]
world.player['beard'] = 'mustache'
world.player['right hand'] = 'spear'
world.player['left hand'] = 'arrow'

for i in range(5):
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
    for entity in world.entityList:
        if entity.hp <= 0:
            entity.action = 1
    
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
