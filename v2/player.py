'''
Created on May 13, 2015

@author: jacobrettig
'''
import pygame

from entity import Mob, Entity
from spriteSheetLPC import LPC
import action


class Player(Mob):
    def __init__(self, *args, **kwargs):
        Mob.__init__(self, *args, **kwargs)
        self._timeRate = 0
        
    @staticmethod
    def DEFAULT(world):
        from world import World
        player = Player(world, (0, 0, 3 * World.SIZE / 6), LPC(hair='plain', shirt='brown', pants='teal', shoes='black'))
        player.acts[0] = action.slash
        player.speed = 2
        return player
    
    def timeRate(self):
        t = self._timeRate
#         self._timeRate = 0
        return t
    
    def _update(self):
        
        pressed = pygame.key.get_pressed()
        
        self.isMoving = pressed[pygame.K_UP] is 1
        if self.isMoving is 1:
            self._timeRate = 1
        left = pressed[pygame.K_LEFT] is 1
        right = pressed[pygame.K_RIGHT] is 1  
        if (left or right) and not (left and right):
            self._timeRate = 1
            if left:
                self.turn(-1)
            else:
                self.turn(1)
        
        Mob._update(self)
          
        if pressed[pygame.K_SPACE] is 1 and self.act is -1:
            self.action = 0
        
        return Entity._update(self)
    