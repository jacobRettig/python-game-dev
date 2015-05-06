
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from collections import Iterable
import math

from vector2d import Vector2D


class Entity():
    def __init__(self, world, x, y, side, speed, turnRate=math.pi/8):
        self.world = world
        self.pos = Vector2D(x, y)
        self.dir = Vector2D(1, 0)
        self.speed = speed
        
        if isinstance(turnRate, Iterable):
            self.turnRate = Vector2D(turnRate[0], turnRate[1])
        else:
            self.turnRate = Vector2D(math.cos(turnRate), math.sin(turnRate))
        self.move = self.movementClass(self)
        
    @staticmethod
    def movementClass(owner):
        class Move(Vector2D):
            def __init__(self):
                pass
            
            @property
            def x(self):
                return self.owner.speed * self.owner.dir.x
            @x.setter
            def x(self, v):
                raise AttributeError
            @property
            def y(self):
                return self.owner.speed * self.owner.dir.y
            @y.setter
            def y(self, v):
                raise AttributeError
            
            def __getitem__(self, k):
                if k == 0:
                    return self.x
                elif k == 1:
                    return self.y
                else:
                    raise AttributeError
            def __setitem__(self, k, v):
                raise AttributeError
            def __iter__(self):
                return (self.x, self.y).__iter__()
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
        return self.pos.x + self.w
    @r.setter
    def r(self, v):
        self.pos.x = v - self.w
        
    @property
    def bottom(self):
        return self.pos.y + self.h
    @bottom.setter
    def bottom(self, v):
        self.pos.y = v - self.h
    @property
    def b(self):
        return self.pos.y + self.h
    @b.setter
    def b(self, v):
        self.pos.y = v - self.h
        
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
    
    
