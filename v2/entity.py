
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from collections import Iterable
import functools
import math, util
from numbers import Number
import random

import action
from gameObject import GameObject
from spriteSheetLPC import AnimationLPC
from square import Square
import square
import util, sys
from vector2d import Vector2D


class Entity(GameObject):
    def __init__(self, world, dim, direction=0, speed=.2, turnRate=math.pi/16, hp=20):
        GameObject.__init__(self, world, dim)
        self._dir = direction
        self.turnRate = turnRate
        self.speed = speed
        
        self.hp = hp
        self.lastTime = self.world.time
                

    def doActionTrigger(self):
        if self.act == -1:
            for i in range(len(self.acts)):
                if self.acts[i].trigger(self):
                    self.action = i
                    break

#     basic movement

    def turn(self, amount=0):
        if self.lastTime != self.world.time:
            self._dir += amount * self.turnRate
    
    @property
    def dir(self):
        return Vector2D(math.cos(self._dir), math.sin(self._dir))
    
    def move(self, isForward=True):
        if isForward:
            self._tl += self.getMovement()
        else:
            self._tl -= self.getMovement()
        
    def getMovement(self):
        return self.dir * self.speed * (self.world.time - self.lastTime)
    def doCollisions(self):
        self.keepInside(self.world.map)
        for tile in self.world.map.solidTiles:
            self.deCollide(tile, self)
    
    def doMovement(self):
        if self.isMoving is True:
            self.move()
        
    
    def update(self):
        self.doMovement()
        self.doCollisions()
        return self.updateWrapUp()
    
    def updateWrapUp(self):
        self.lastTime = self.world.time
        
    
    

    
    
    
class Mob(Entity):
    def __init__(self, world, dim, direction=0, speed=.6, turnRate=math.pi/10, visDistance=50, visAng=math.pi/2, hearDistance=30,
         hp=20):
        Entity.__init__(self, world, dim, direction, speed, turnRate, hp)
        self.isAlive = True
        self.isMoving = False
        self.isActing = False
        self.sightDistance = 100 ** 2
        self.act = -1
        self.acts = [action.death]
        self.blurbs = {
                       'text':[],
                       'current':-1,
                       'time':self.world.time + random.random() * 50
                       }
        
        self.animation = AnimationLPC(self)
        
        self.visAng = visAng
        self.visDistance = (visDistance + self.side) ** 2
        self.hearDistance = (hearDistance + self.side) ** 2
        self.seen = set()
    
    @property
    def blurb(self):
        if self.world.time >= self.blurbs['time']:
            self.blurbs['current'] = random.randint(0, len(self.blurbs['text'])) - 1
            self.blurbs['time'] = self.world.time + random.random() * 50
        if self.blurbs['current'] is -1:
            return ''
        else:
            return self.blurbs['text'][self.blurbs['current']]
        
    @property
    def image(self):
        return self.animation.image
    
    @property
    def imagePosition(self):
        image = self.image
        return (self.cx - image.get_width()/2, self.oy - image.get_height())
    
    @property
    def action(self):
        if self.act is not -1 and self.acts[self.act].action is not None:
            if self.cycles != self.animation.cycles:
                self.cycles = self.animation.cycles
                self.acts[self.act].onCycle(self)
            
            self._timeRate = 1
            return self.acts[self.act].action
        elif self.isMoving:
            return 'walk'
        else:
            return 'none'
    @action.setter
    def action(self, value):
        self.cycles = 0
        self.animation.time = self.lastTime
        self.animation.cycles = 0
        self.act = value
        if self.act is not -1:
            self.acts[self.act].onStart(self)
        
    def update(self):
        self.doSight()
        Entity.update(self)
        return not self.isAlive
    
    def doSight(self):
        self.seen = self.sight()
        for seen in self.world.entityList:
            if seen in self.seen or seen.cen.gethypot(self.cen) <= self.hearDistance:
                self.onSight(seen)
            
    def __getitme__(self, k):
        return self.animation[k]
    
    def __setitem__(self, k, v):
        self.animation[k] = v
        
    
    @util.InstanceGuard('_visVec', 'set')
    def visVec(self, val):
        self._visVec = Entity.normVector(val)
        
#     Make read-only
    visL = util.InstanceGuard('_visL', None)
    visR = util.InstanceGuard('_visR', None)
    

#     ROUGH as in very rough first version of the vision method 
    def sight(self):
        seen = set()
        cen = self.cen()
        for E in self.world.entityList:
            if self != E:
                ang = abs(((cen - E.cen).angle + math.pi) % (2 * math.pi))
                if ang <= self.visAng or ang >= 2 * math.pi - self.visAng:
                    if (cen - E.cen).hypot <= self.sightDistance:
                        seen.add(E)
        return seen
    
    def onSight(self, target):
        pass
