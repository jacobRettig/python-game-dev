
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from collections import Iterable
import math

from vector2d import Vector2D

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


class Entity():
    def __init__(self, world, x, y, side, speed, turnRate=math.pi/8):
        self.world = world
        self.pos = Vector2D(x, y)
        self._dir_ = Vector2D(1, 0)
        self.speed = speed
        self.isOpaque = False
        self.cen = self.centerClass(self)
        self.opposite = self.OppositeClass(self)
        
        if isinstance(turnRate, Iterable):
            self.turnRate = Vector2D(turnRate[0], turnRate[1])
        else:
            self.turnRate = Vector2D(math.cos(turnRate), math.sin(turnRate))
        self.move = self.movementClass(self)
        
    @property
    def dir(self):
        return self._dir_
    @dir.setter
    def dir(self, v):
        self._dir_ = self.directionClass(self, *v)
        
    @property
    def cx(self):
        return self.cen.x
    @cx.setter
    def cx(self, v):
        self.cen.x = v
    @property
    def cy(self):
        return self.cen.y
    @cy.setter
    def cy(self, v):
        self.cen.y = v
    
    @property
    def ox(self):
        return self.opposite.x
    @ox.setter
    def ox(self, v):
        self.opposite.x = v
    @property
    def oy(self):
        return self.opposite.y
    @oy.setter
    def oy(self, v):
        self.opposite.y = v
    
    @staticmethod
    def OppositeClass(owner):
        class Opposite(Vector2D):
            def __init__(self):
                pass    
            @property
            def x(self):
                return self.owner.x + self.owner.side
            @x.setter
            def x(self, v):
                self.owner.x = v - self.owner.side
            @property
            def y(self):
                return self.owner.y + self.owner.side
            @y.setter
            def y(self, v):
                self.owner.y = v - self.owner.side
            
            def __call__(self):
                return Opposite()
            
            def __getitem__(self, k):
                if k == 0:
                    return self.x
                elif k == 1:
                    return self.y
                else:
                    raise IndexError
            def __setitem__(self, k, v):
                if k == 0:
                    self.x = v
                elif k == 1:
                    self.y = v
                else:
                    raise IndexError
            def __iter__(self):
                return tuple(self.x, self.y).__iter__()
        return Opposite()
    
    @staticmethod
    def directionClass(owner, *params):
        class Direction(Vector2D):
            VALUE_ACCURACY = 0.0001
            
            @property
            def AccError(self):
                class AccuracyError(Exception):
                    pass
                return AccuracyError("outside of length limits : {a}    Hypot : {b}".format(a=self.VALUE_ACCURACY,
                            b=self.hypot))
            
            def accTest(self):
                if abs(self.x**2 + self.y**2) - 1 > self.VALUE_ACCURACY:
                    raise self.AccError
            
            def __init__(self, *args):
                Vector2D.__init__(self, *args)
                self.accTest()
            
            
            def __call__(self):
                return Direction(self.x, self.y)
            
            def __setitem__(self, k, v):
                Vector2D.__setitem__(self, k, v)
                self.accTest()
                
            def __iter__(self):
                return tuple(self.x, self.y).__iter__()
        return Direction(owner, *params)
        
    @staticmethod
    def centerClass(owner):
        class Center(Vector2D):
            def __init__(self):
                pass    
            @property
            def x(self):
                return owner.x + self.owner.side/2
            @x.setter
            def x(self, v):
                owner.x = v - self.owner.side/2
            @property
            def y(self):
                return owner.y + self.owner.side/2
            @y.setter
            def y(self, v):
                owner.y = v - self.owner.side/2
            
            def __call__(self):
                return Center()
            
            def __getitem__(self, k):
                if k == 0:
                    return self.x
                elif k == 1:
                    return self.y
                else:
                    raise IndexError
            def __setitem__(self, k, v):
                if k == 0:
                    self.x = v
                elif k == 1:
                    self.y = v
                else:
                    raise IndexError
            def __iter__(self):
                return tuple(self.x, self.y).__iter__()
        return Center()
    
    @staticmethod
    def movementClass(owner):
        class Move(Vector2D):
            def __init__(self):
                pass
            
            @property
            def x(self):
                return owner.speed * self.owner.dir.x
            @x.setter
            def x(self, v):
                raise AttributeError
            @property
            def y(self):
                return owner.speed * self.owner.dir.y
            @y.setter
            def y(self, v):
                raise AttributeError
            
            def __call__(self):
                return Move()
            
            def __getitem__(self, k):
                if k == 0:
                    return self.x
                elif k == 1:
                    return self.y
                else:
                    raise IndexError
            def __setitem__(self, k, v):
                raise AttributeError
            def __iter__(self):
                return tuple(self.x, self.y).__iter__()
        return Move()
        
    @property
    def x(self):
        return self.pos.x
    @x.setter
    def x(self, v):
        self.pos.x = v
    @property
    def left(self):
        return self.pos.x
    @left.setter
    def left(self, l):
        self.pos.x = l
    @property
    def l(self):
        return self.pos.x
    @l.setter
    def l(self, l):
        self.pos.x = l
    
    @property
    def y(self):
        return self.pos.y
    @y.setter
    def y(self, y):
        self.pos.y = y
    @property
    def top(self):
        return self.pos.y
    @top.setter
    def top(self, y):
        self.pos.y = y
    @property
    def t(self):
        return self.pos.y
    @t.setter
    def t(self, y):
        self.pos.y = y
        
    @property
    def right(self):
        return self.pos.x + self.s
    @right.setter
    def right(self, v):
        self.pos.x = v - self.s
    @property
    def r(self):
        return self.pos.x + self.s
    @r.setter
    def r(self, v):
        self.pos.x = v - self.s
        
    @property
    def bottom(self):
        return self.pos.y + self.s
    @bottom.setter
    def bottom(self, v):
        self.pos.y = v - self.s
    @property
    def b(self):
        return self.pos.y + self.s
    @b.setter
    def b(self, v):
        self.pos.y = v - self.s
        
    def isInside(self, other):
        if isinstance(other, Entity):
            return other.r >= self.l and other.b >= self.t and other.l <= self.r and other.t <= self.b
        elif isinstance(other, Vector2D):
            return other.x >= self.l and other.x <= self.r and other.y >= self.t and other.y <= self.b
        else:
            raise AttributeError

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
        
        
        
    
            

