
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from collections import Iterable
import math

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





class Entity(GameObject):
    def __init__(self, world, pos, direction=(1,0), speed = 5, turnRate=math.pi/16):
        GameObject.__init__(self, world, pos)
        self.dir = direction
        self.speed = speed
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
            
        
    @property
    def dx(self):
        return self.move.x
    @dx.setter
    def dx(self, v):
        self.move.x = v

    @property
    def dy(self):
        return self.move.y
    @dy.setter
    def dy(self, v):
        self.move.y = v
        
    @property    
    def image(self):
        return None
    @image.setter
    def image(self, v):
        raise AttributeError
    
    def destroy(self):
        self.owner.entityList.remove(self)
        
    #TODO
    def update(self):
        return False
    
    
class EntitySight(Entity):
    def __init__(self, world, x, y, side, speed, turnRate=math.pi/8, sightVec=(math.sqrt(2)*5, math.sqrt(2)*5)):
        Entity.__init__(self, world, x, y, side, speed, turnRate)
        
        self.sightVec = Vector2D(*sightVec)
    
    def seen(self):
        cl = self.dir.angleAdd(self.sightVec)
        cr = self.dir.angleSub(self.sightVec)
        x1, x2 = min(0, cl.x, cr.x) + self.cx, max(0, cl.x, cr.x) + self.cx
        y1, y2 = min(0, cl.y, cr.y) + self.cy, max(0, cl.y, cr.y) + self.cy
        
        Es = tuple()
        for E in self.world.getVisibleSection(self, (x1, y1, x2, y2)):
            Es += (self.visibleLines(E),)
            
#         1: a > b    0:a == b    -1:a < b
        def compare(a, b):
            if a[3] == b[3] and a[4] == b[4]:
                return 0
            if a[3] < 0 ^ b[3] < 0:
                if a[3] < 0:
                    return -1
                else:
                    return 1
            if a[3] * b[4] > a[4] * b[3]:
                if a[3] < 0:
                    return 1
                else:
                    return -1
            else:
                if a[3] < 0:
                    return -1
                else:
                    return 1
            
        seen = []
        pre, post = [], []
        for E in Es:
            if None in E:
                seen.append(E)
            elif E[2].sinSub(cr) > 0 and E[2].sinSub(cl) < 0:
                binaryInsertionSort(compare, pre, E + E[1].angleSub(cr))
            elif E[1].sinSub(cr) > 0 and E[1].sinSub(cl) < 0:
                binaryInsertionSort(compare, post, E + E[2].angleSub(cr))
        
#         checks if inside any opaque objects
        for E in seen:
            if E[0].isOpaque:
                return seen
        
        

        

#     returns (E, left, right)
    def visibleLines(self, E):
        x, y = 2, 2
        
        if E.x < self.cx:
            if E.x + E.side > self.cx:
                x = 1
            else:
                x = 0
        if E.y < self.cy:
            if E.y + E.side > self.cy:
                y = 1
            else:
                y = 0
        
        corners = (1, 2)
        if x == 0:
            if y == 0:
                corners = (2, 1)
            elif y == 1:
                corners = (3, 1)
            else:
                corners = (3, 0)
        if x == 1:
            if y == 0:
                corners = (2, 3)
            elif y == 1:
                corners = (-0, -0)
            else:
                corners = (1, 0)
        else:
            if y == 0:
                corners = (0, 3)
            elif y == 1:
                corners = (0, 2)
        
        if -1 in corners:
            return (E, None, None)
        else:
            cnr = (E.pos, E.pos + (E.side, 0), E.pos + (0, E.side), E.opposite)
            return (E, cnr[corners[0]] - self.cen, cnr[corners[1]] - self.cen)
        
        
        
    
            

