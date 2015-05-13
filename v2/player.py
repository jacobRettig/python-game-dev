'''
Created on May 13, 2015

@author: jacobrettig
'''
import pygame

from library.v2.entity import Mob
from library.v2.spriteSheetLPC import AnimationLPC


class Player(Mob):
    @staticmethod
    def DEFAULT(world):
        return Player(world, (1, 1, 5), AnimationLPC(self, hair='plain', shirt='brown', pants='teal', shoes='black'))
    
    def update(self):
        pressed = pygame.key.get_pressed()
        
        self.isMoving = pressed[pygame.K_UP]
        
        if pressed[pygame.K_LEFT] ^ pressed[pygame.K_RIGHT]:
            if pressed[pygame.K_LEFT]:
                self.turn(1)
            else:
                self.turn(-1)
        
        return Mob.update(self)
    