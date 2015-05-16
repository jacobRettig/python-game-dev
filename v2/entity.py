
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from collections import Iterable
import functools
import math, util
from numbers import Number
import random

from gameObject import GameObject
from spriteSheetLPC import AnimationLPC
from square import Square
import square
from vector2d import Vector2D
import util







def deltaInstance(owner):
    @util.Vector2DCustom
    def delta(self, k):
        if k == 0 or k == 'x':
            return owner.dir.x * owner.speed
        elif k == 1 or k == 'y':
            return owner.dir.x * owner.speed
        else:
            raise IndexError

    return delta

class Entity(GameObject):
    def __init__(self, world, dim, direction=(1,0), speed=.2, turnRate=math.pi/16, hp=20):
        GameObject.__init__(self, world, dim)
        self.dir = direction
        self.turnRate = turnRate
        self.speed = speed
        self._delta = deltaInstance(self)
        
        self.hp = hp
        self.lastTime = self.world.time
                
    delta = util.InstanceGuard('_delta', None)
    @util.InstanceGuard('_turnRate', 'set')
    def turnRate(self, val):
        self._turnRate = Entity.normVector(val)
    @util.InstanceGuard('_dir', 'set')
    def dir(self, val):
        self._dir = Entity.normVector(val)
    
    dx = util.GS('x', 'delta')
    dy = util.GS('y', 'delta')

#     basic movement

    def turn(self, amount=0):
        if self.lastTime != self.world.time:
            if amount > 0:
                for i in range(amount):
                    self.dir = self.dir.angleAdd(self.turnRate)
            else:
                for i in range(abs(amount)):
                    self.dir = self.dir.angleSub(self.turnRate)
    
    def move(self, amount=0):    
        self.tl += self.delta * amount * (self.world.time - self.lastTime)
    
    def update(self):
        val = self._update()
        self.lastTime = self.world.time
        return val
    
    def _update(self):
        if self.isMoving is True:
            self.move(1)
            
            for i in (self.onCollision(tile) for tile in self.world.map[self.tl : self.br]):
                print(i)
#                   list((self.onCollision(obj) for obj in self.world.entityList if obj in self)))
            if functools.reduce((lambda x, y: x is True or y is True),
                  list((self.onCollision(tile) for tile in self.world.map[self.tl : self.br])) +
                  list((self.onCollision(obj) for obj in self.world.entityList if obj in self and obj is not self))):
                print('collision')
                self.move(-1)
        
        return self.hp < 0
    
    @staticmethod
    def normVector(val):
        try:
            if len(val) != 2:
                raise TypeError
            else:
                val = util.Vector2DReadOnly(*val)
                if abs(val.hypot - 1) > 0.00001:
                    val = math.atan2(val[1], val[0])
                    raise TypeError
        except TypeError:
            if isinstance(val, Number):
                val = util.Vector2DReadOnly(math.cos(val), math.sin(val))
            else:
                raise TypeError("val : {} type : {}".format(val, type(val)))
        except:
            raise Exception("Uknown Exception val : {} type : {}".format(val, type(val)))
        finally:
            return val
    
    
    
    
    

    
    
    
    
def visLInstance(owner):
    @util.Vector2DCustom
    def visL(self, k):
        if k == 0 or k == 'x':
            return owner.dir.angleAdd(owner.visVec).x * owner.visDis
        elif k == 1 or k == 'y':
            return owner.dir.angleAdd(owner.visVec).y * owner.visDis
        else:
            raise IndexError
    return visL

def visRInstance(owner):
    @util.Vector2DCustom
    def visR(self, k):
        if k == 0 or k == 'x':
            return owner.dir.angleSub(owner.visVec).x * owner.visDis
        elif k == 1 or k == 'y':
            return owner.dir.angleSub(owner.visVec).y * owner.visDis
        else:
            raise IndexError
    return visR



    
    
class Mob(Entity):
    def __init__(self, world, dim, spriteSheet, direction=(1,0), speed=.3, turnRate=math.pi/16, visDis=6, visVec=(math.sqrt(2),)*2,
         hp=20):
        Entity.__init__(self, world, dim, direction, speed, turnRate, hp)
        self.isMoving = False
        self.isActing = False
        self.act = -1
        self.acts = util.ScalingList()
        self.blurbs = {
                       'text':[],
                       'current':-1,
                       'time':self.world.time + random.random() * 50
                       }
        
        self.animation = AnimationLPC(self, spriteSheet)
        print(dir(self.animation))
        
        self.visDis = visDis
        self.visVec = visVec
        self._visL = visLInstance(self)
        self._visR = visRInstance(self)
    
    @property
    def blurb(self):
        if self.world.time >= self.blurbs['time']:
            self.blurbs['current'] = random.randint(0, len(self.blurbs['text'])) - 1
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
        return (self.cx - image.get_width()/2, self.cy - image.get_height())
    
    @property
    def action(self):
        if self.act is not -1 and self.acts[self.act].action is not None:
            if self.cycles != self.animation.cycles:
                self.cycles = self.animation.cycles
                self.acts[self.act].onCycle(self)
                
            return self.acts[self.act].action
        elif self.isMoving:
            return 'walk'
        else:
            return 'none'
    @action.setter
    def action(self, value):
        self.cycles = 0
        self.act = value
        if self.act is not -1:
            self.acts[self.act].onStart(self)
        
#     return True if movement should be undone
    def onCollision(self, obstacle):
        return obstacle.isSolid
    
    def _update(self):
        self.seen = self.sight()
        for seen in self.sight():
            self.onSight(seen)
        
        return Entity._update(self)
    
    @property
    def time(self):
        return self.world.time
        
    @util.InstanceGuard('_visVec', 'set')
    def visVec(self, val):
        self._visVec = Entity.normVector(val)
        
#     Make read-only
    visL = util.InstanceGuard('_visL', None)
    visR = util.InstanceGuard('_visR', None)
    

#     ROUGH as in very rough first version of the vision method 
    def sight(self):
        x = (0, self.visL.x, self.visR.x)
        y = (0, self.visL.y, self.visR.y)
        sq = Square((min(x), min(y), max(max(x) - min(x), max(y) - min(y))))
        cen = self.cen()
        
        sR = self.visR
        sL = self.visL.angleSub(sR).angle
        
        sq += cen
        
        boundingRect = self.world.map[self.tl : self.br]
        for obj in self.world.entityList:
            if obj in sq:
                boundingRect.append(obj)
                
        keepGoing = True
        seen = []
        rangedList = []
        fn = (lambda x, y: x[2] - y[2])
        for obj in boundingRect:
            try:
                oL, oR = obj.normalProjection(cen)
                oL = oL.angleSub(sR).angle
                oR = oR.angleSub(sR).angle
                if oR >= 0 and oR <= sL:
                    rangedList = util.binaryInsertionSort(fn, rangedList, (obj, min(sL, oL), oR))
                elif oL >= 0 and oL <= sL:
                    rangedList = util.binaryInsertionSort(fn, rangedList, (obj, oL, max(0, oR)))
            except square.InvalidGeometry:
                seen.append(obj)
                if obj.isOpaque:
                    obj.keepGoing = False
                    
        if keepGoing is False:
            return seen
        
        for obj in rangedList:
            ang = obj[2]
            success = True
            disCheck = obj[0].hypot(cen)
            for obstacle in rangedList:
                if not obj is obstacle:
                    if ang < obstacle[2]:
                        break
                    elif obstacle[0].isOpaque and ang < obstacle[1] and obstacle[0].hypot(cen) < disCheck:
                        ang = obstacle[1]
                        if ang > obj[1]:
                            success = False
                            break
                        
            if success:
                seen.append(obstacle[0])
                
        return seen
    
    def onSight(self, target):
        pass
