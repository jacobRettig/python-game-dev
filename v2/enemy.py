'''
Created on Apr 29, 2015

@author: jacobrettig
'''

import math

import pygame

import action
from entity import Mob, Entity
from player import Player


class Enemy(Mob):
    def __init__(self, world, dim, spriteSheet, *args, **kwargs):
        Mob.__init__(self, world, dim, spriteSheet, *args, **kwargs)
        self.isMoving = False
        self.target = self.cen()
#         self.acts[0] = action.slash
#         self.acts[1] = action.stab
        
    def AITurn(self):
        ang = self.dir.angleSub(self.target - self.cen)
        if ang.y < 0:
            if ang.sinAdd(self.turnRate) <= 0:
                return 1
        else:
            if ang.sinSub(self.turnRate) >= 0:
                return -1
        return 0
    
    def AIMove(self):
        cen = self.cen()
        if (cen + self.getMovement()).gethypot(self.target) < cen.gethypot(self.target):
            self.move(True)
            return True
        else:
            return False
    
    def onSight(self, target):
        if isinstance(target, Player):
            self.target = target.cen
            
#             if self.act is -1:
#                 hypot = self.hypot(target)
#                 if hypot <= 10:
#                     self.action = 1
#                 elif hypot <= 15:
#                     self.action = 0
                    
    
    def update(self):
        self.turn(self.AITurn())
        self.doSight()
        self.isMoving = self.AIMove()
        self.doCollisions()
        if pygame.key.get_pressed()[pygame.K_q]:
            self.action = 0
        if Entity.updateWrapUp(self):
            self.action = 0
        return not self.isAlive
        
    
