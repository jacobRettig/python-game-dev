'''
Created on Apr 29, 2015

@author: jacobrettig
'''

import math
from entity import Mob
from library.v2.player import Player
import action

class Enemy(Mob):
    def __init__(self, world, dim, spriteSheet, *args, **kwargs):
        Mob.__init__(world, dim, spriteSheet, *args, **kwargs)
        self.target = self.cen()
        self.acts[0] = action.slash
        self.acts[1] = action.stab
        
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
        return (self.cen - self.target + self.delta).hypot < (self.cen - self.target).hypot
    
    def onSight(self, target):
        if isinstance(target, Player):
            self.target = target.cen
            
            if self.act is -1:
                hypot = self.hypot(target)
                if hypot <= 10:
                    self.action = 1
                elif hypot <= 15:
                    self.action = 0
                    
    
    def _update(self):
        self.turn(self.AITurn())
        self.isMoving = self.AIMove()
        return Mob._update(self)
        
    
