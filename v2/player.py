'''
Created on May 13, 2015

@author: jacobrettig
'''
import pygame

import action
from entity import Mob
from spriteSheetLPC import LPC


class Player(Mob):
    def __init__(self, *args, **kwargs):
        Mob.__init__(self, *args, **kwargs)
        self._timeRate = 0
        
    def __hash__(self):
        return id(self)
        
    @staticmethod
    def DEFAULT(world):
        from world import World
        player = Player(world, (0, 0, 3 * World.SIZE / 6), LPC(hair='plain', shirt='brown', pants='teal', shoes='black'))
        player.acts = [action.shove]
        player.speed = 2
        print(hash(player))
        return player
    
    def timeRate(self):
        t = self._timeRate
        self._timeRate = 0
        return t
    
    def update(self):
        
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_SPACE] is 1 and self.act is -1:
            self.action = 0
        
        if self.act is 0:
            self._timeRate = 0
        else:
            if 1 in (pressed[pygame.K_UP], pressed[pygame.K_LSHIFT], pressed[pygame.K_LEFT], pressed[pygame.K_RIGHT]):
                self._timeRate = 1
            else:
                self._timeRate = 0
        
            if pressed[pygame.K_UP] is 1:
                self.isMoving = True
            elif self._timeRate is 0:
                self.isMoving = False
                
            left = pressed[pygame.K_LEFT] is 1
            right = pressed[pygame.K_RIGHT] is 1  
            if (left or right) and not (left and right):
                if left:
                    self.turn(-1)
                else:
                    self.turn(1)
        
        return Mob.update(self)