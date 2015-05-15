'''
Created on May 13, 2015

@author: jacobrettig
'''
import pygame

from entity import Mob, Entity
from spriteSheetLPC import AnimationLPC
import action


class Player(Mob):
    def __init__(self, *args, **kwargs):
        Mob.__init__(self, *args, **kwargs)
        self._timeRate = 0
        
    @staticmethod
    def DEFAULT(world):
        player = Player(world, (1.5, 1.5, .6), AnimationLPC(world, hair='plain', shirt='brown', pants='teal', shoes='black'))
        player.acts[0] = action.slash
        return player
    
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
        
        Mob._update(self)
          
        if pressed[pygame.K_SPACE] and self.act is -1:
            self.action = 0
        
        return Entity._update(self)
    