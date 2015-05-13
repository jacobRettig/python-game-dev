'''
Created on Apr 29, 2015

@author: jacobrettig
'''

import math
from entity import MobSight
from library.v2.player import Player

class Enemy(MobSight):
    def __init__(self, world, dim, spriteSheet, direction=(1,0), speed=5, turnRate=math.pi/16, visDis=6, visVec=(1,0), hp=20):
        MobSight.__init__(world, dim, spriteSheet, direction, speed, turnRate, visDis, visVec)
        self.target = self.cen()
        
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
    
    def update(self):
        self.turn(self.AITurn())
        self.isMoving = self.AIMove()
        return MobSight.update(self)
        
    
