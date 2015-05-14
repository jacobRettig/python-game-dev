'''
Created on May 13, 2015

@author: jacobrettig
'''
import pygame

from library.v2.entity import Mob
from library.v2.spriteSheetLPC import AnimationLPC


class Player(Mob):
    def __init__(self, *args, **kwargs):
        Mob.__init__(self, *args, **kwargs)
        self._timeRate = 0
        
    @staticmethod
    def DEFAULT(world):
        return Player(world, (1, 1, 5), AnimationLPC(self, hair='plain', shirt='brown', pants='teal', shoes='black'))
    
    def timeRate(self):
        t = self._timeRate
        self._timeRate = 0
        return t
    
    def _update(self):
        pressed = pygame.key.get_pressed()
        
        self.isMoving = pressed[pygame.K_UP]
        if self.isMoving:
            self._timeRate = 1
        
        if pressed[pygame.K_LEFT] ^ pressed[pygame.K_RIGHT]:
            self._timeRate = 1
            if pressed[pygame.K_LEFT]:
                self.turn(1)
            else:
                self.turn(-1)
        
        return Mob.update(self)
    