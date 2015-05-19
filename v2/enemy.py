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
    def __init__(self, world, dim, *args, **kwargs):
        Mob.__init__(self, world, dim, *args, **kwargs)
        self.isMoving = False
        self.target = self.cen()
#         self.acts[0] = action.slash
#         self.acts[1] = action.stab
        
    def AITurn(self):
        return max(min((self.target - self.cen).angle, -self.turnRate), self.turnRate) 
    
    def AIMove(self):
        cen = self.cen()
        if (cen + self.getMovement()).gethypot(self.target) < cen.gethypot(self.target):
            self.move(True)
            return True
        else:
            return False
    
    def onSight(self, target):
        if target == self.world.player:
            self.target = target.cen()
            
    
    def update(self):
        self.doActionTrigger()
        self.doSight()
        if self.act == -1 and self.lastTime != self.world.time:
            self.turn(self.AITurn())
            self.isMoving = self.AIMove()
            self.doCollisions()
        self.updateWrapUp()
        return not self.isAlive
        
    
