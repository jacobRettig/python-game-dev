
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from collections import Iterable
import math, util

from vector2d import Vector2D
from square import Square
from gameObject import GameObject
from numbers import Number

def binaryInsertionSort(compareFunction, sortList, *items):
    if len(sortList) == 0 and len(items) != 0:
        sortList.append(items.pop())
    count = len(sortList)
    for item in items:
        low, high = 0, count
        while low < high:
            mid = (low + high) / 2
            comparison = compareFunction(sortList[mid], item)
            if comparison == 0:
                low, high = mid, mid
            elif comparison < 0:
                low = mid + 1
            else:
                high = mid - 1
        sortList.insert(low, item)
        count += 1
    return sortList


def deltaInstance(owner):
    class Delta(util.Vector2DReadOnly):
        def __init__(self):
            pass
        
#         override normal Vector stuff to prevent unnecessary crashes
        def __len__(self):
            return 2
        
        def __getitem__(self, k):
            if k == 0 or k == 'x':
                return owner.dir.x * owner.speed
            elif k == 1 or k == 'y':
                return owner.dir.x * owner.speed
            else:
                raise IndexError

        @property
        def list(self):
            return [self.x, self.y]
        
        def __iter__(self):
            return self.list.__iter__()
        
#         remove reference and just use as a normal point
        def __call__(self):
            return Vector2D(self.x, self.y)    
#    return the class with it's local scope saved
    return Delta()



class Entity(GameObject):
    
    def __init__(self, world, pos, direction=(1,0), speed = 1, turnRate=math.pi/16, hp=20):
        GameObject.__init__(self, world, pos)
        self.dir = direction
        self.turnRate = turnRate
        self.speed = speed
        self._delta = deltaInstance(self)
        
        self.hp = hp
                
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
        if amount > 0:
            for i in range(amount):
                self.dir = self.dir.angleAdd(self.turnRate)
        else:
            for i in range(abs(amount)):
                self.dir = self.dir.angleSub(self.turnRate)
    
    def move(self, amount=0):    
        self.tl += self.delta*amount
    
    def update(self):
        return self.hp < 20
    
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
    class VisLVec(util.Vector2DReadOnly):
        def __init__(self):
            pass
        
#         override normal Vector stuff to prevent unnecessary crashes
        def __len__(self):
            return 2
        
        def __getitem__(self, k):
            if k == 0 or k == 'x':
                return owner.dir.angleAdd(owner.visVec).x * owner.visDis
            elif k == 1 or k == 'y':
                return owner.dir.angleAdd(owner.visVec).y * owner.visDis
            else:
                raise IndexError

        @property
        def list(self):
            return [self.x, self.y]
        
        def __iter__(self):
            return self.list.__iter__()
        
#         remove reference and just use as a normal point
        def __call__(self):
            return Vector2D(self.x, self.y)    
#    return the class with it's local scope saved
    return VisLVec()

def visRInstance(owner):
    class VisRVec(util.Vector2DReadOnly):
        def __init__(self):
            pass
        
#         override normal Vector stuff to prevent unnecessary crashes
        def __len__(self):
            return 2
        
        def __getitem__(self, k):
            if k == 0 or k == 'x':
                return owner.dir.angleSub(owner.visVec).x * owner.visDis
            elif k == 1 or k == 'y':
                return owner.dir.angleSub(owner.visVec).y * owner.visDis
            else:
                raise IndexError

        @property
        def list(self):
            return [self.x, self.y]
        
        def __iter__(self):
            return self.list.__iter__()
        
#         remove reference and just use as a normal point
        def __call__(self):
            return Vector2D(self.x, self.y)    
#    return the class with it's local scope saved
    return VisRVec()




    
class EntitySight(Entity):
    def __init__(self, world, pos, direction=(1,0), speed=5, turnRate=math.pi/16, visDis=6, visVec=(1,0), hp=20):
        Entity.__init__(self, world, pos, direction, speed, turnRate, hp=20)
        self.visDis = visDis
        self.visVec = visVec
        self._visL = visLInstance(self)
        self._visR = visRInstance(self)
        
    @util.InstanceGuard('_visVec', 'set')
    def visVec(self, val):
        self._visVec = Entity.normVector(val)
        
#     Make read-only
    visL = util.InstanceGuard('_visL', None)
    visR = util.InstanceGuard('_visR', None)
    

#     ROUGH as in very rough first version of the vision method 
    def sight(self):
        x = (0, visL.x, visR.x)
        y = (0, visL.y, visR.y)
        sq = Square((min(x), min(y), max(max(x) - min(x), max(y) - min(y))))
        cen = self.cen()
        
        sR = self.visR
        sL = self.visL.angleSub(sR).angle
        
        sq += cen
        
        
        boundingRect = []
        for obj in self.world.WorldObjectList:
            if obj in sq:
                boundingRect.append(obj)
                
        keepGoing = True
        seen = []
        rangedList = []
        for obj in boundingRect:
            try:
                oL, oR = obj.normalProjection(cen)
                oL = oL.angleSub(sR).angle
                oR = oR.angleSub(sR).angle
                if oR >= 0 and oR <= sL:
                    rangedList.append((obj, min(sL, oL), oR))
                elif oL >= 0 and oL <= sL:
                    rangedList.append((obj, oL, max(0, oR)))
            except square.InvalidGeometry:
                seen.append(obj)
                if obj.isOpaque:
                    obj.keepGoing = False
                    
        fn = (lambda x, y: x[2] - y[2])
        rangedList = binaryInsertionSort(fn, [], *rangedList)
        
        for obj in rangedList:
            ang = obj[2]
            success = True
            disCheck = obj[0].cen.getdistance(cen) - obj[0].side
            for obstacle in rangedList:
                if not obj is obstacle:
                    if ang < obstacle[2]:
                        break
                    elif obstacle[0].isOpaque and ang < obstacle[1] and obstacle[0].cen.getdistance(cen) \
                      - obstacle[0].side < disCheck:
                        ang = obstacle[1]
                        if ang > obj[1]:
                            success = False
                            break
                        
            if success:
                seen.append(obstacle[0])
        return seen
    
    def onSight(self, target):
        pass
    
    def update(self):
        return Entity.update(self)
