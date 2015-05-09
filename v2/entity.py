
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
    for item in items:
        low, high = 0, len(sortList) - 1
        while low != high:
            mid = (low + high) // 2
            comparison = compareFunction(sortList[mid], item)
            if comparison == 0:
                low, high = mid, mid
            elif comparison > 0:
                high = mid - 1
            else:
                low = mid - 1
                
        sortList.insert(low, item)
    return sortList


def deltaInstance(owner):
    class Delta(Vector2D):
        def __init__(self):
            pass
        
#         getters and setters for x&y
        @property
        def x(self):
            return owner.dir.x * owner.speed
            
        @property
        def y(self):
            return owner.dir.y * owner.speed
            
#         override normal Vector stuff to prevent unnecessary crashes
        def __len__(self):
            return 2
        
        def __getitem__(self, k):
            if k == 0 or k == 'x':
                return self.x
            elif k == 1 or k == 'y':
                return self.y
            else:
                raise IndexError
        def __setitem__(self, k, v):
            if k == 0 or k == 'x':
                self.x = v
            elif k == 1 or k == 'y':
                self.y = v
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
    def __init__(self, world, pos, direction=(1,0), speed = 5, turnRate=math.pi/16):
        GameObject.__init__(self, world, pos)
        self.dir = direction
        self.speed = speed
        self._delta = deltaInstance(self)
        try:
            if len(turnRate) != 2:
                raise TypeError
            else:
                self.turnRate = Vector2D(*turnRate)
                if abs(self.turnRate.hypot - 1) > 0.00001:
                    turnRate = math.atan2(turnRate.y, turnRate.x)
                    raise TypeError
        except TypeError:
            if isinstance(turnRate, Number):
                self.turnRate = Vector2D(math.cos(turnRate), math.sin(turnRate))
            else:
                raise TypeError("type : {}".format(type(turnRate)))
            
            
    delta = util.InstanceGuard('_delta', None)
        
    dx = util.GS('x', 'delta')
    dy = util.GS('y', 'delta')

    
class EntitySight(Entity):
    def __init__(self, world, x, y, side, speed, turnRate=math.pi/8, sightVec=(math.sqrt(2)*5, math.sqrt(2)*5)):
        Entity.__init__(self, world, x, y, side, speed, turnRate)
        
        self.sightVec = Vector2D(*sightVec)
    
   
        
        
    
            

