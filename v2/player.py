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
        player = Player(world, (0, 0, 3 * World.SIZE / 6))
        player['hair'] = 'plain'
        player['shirt'] = 'brown'
        player['pants'] = 'teal'
        player['shoes'] = 'black'
        
        
        from action import Action
        @Action('slash')
        def attack(self, owner):
            owner.isMoving = False
            from entity import Mob
            for seen in owner.seen:
                if isinstance(seen, Mob) and seen.hypot(owner.cen) <= 15:
                    seen.hp -= 2
                    
        import pygame
        attack.pygame = pygame
        
        @attack.setTrigger
        def attack(self, owner):
            return self.pygame.key.get_pressed()[pygame.K_SPACE] == 1
            
            
        player.acts = [attack]
        player.speed = 2
        return player
    
    def timeRate(self):
        if not self.isAlive:
            return 1
        t = self._timeRate
        self._timeRate = 0
        return t
    
    def update(self):
        
        pressed = pygame.key.get_pressed()
        
        self.doActionTrigger()
        
        self._timeRate = 0
        if self.act != -1:
            self._timeRate = 0
        else:
            if 1 in (pressed[pygame.K_UP], pressed[pygame.K_LSHIFT], pressed[pygame.K_LEFT], pressed[pygame.K_RIGHT]):
                self._timeRate = 1
            else:
                self._timeRate = 0
        
            self.isMoving = pressed[pygame.K_UP] == 1
            
            left = pressed[pygame.K_LEFT] == 1
            right = pressed[pygame.K_RIGHT] == 1  
            if (left or right) and not (left and right):
                if left:
                    self.turn(-1)
                else:
                    self.turn(1)
        
        return Mob.update(self)