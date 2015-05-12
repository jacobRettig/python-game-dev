'''
Created on Apr 20, 2015

@author: jacobrettig
'''

import math

from vector import Vector


class Vector2D(Vector):
    def __init__(self, x=0, y=0):
        Vector.__init__(self, x, y)
    @property
    def x(self):
        return self[0]
    @property
    def y(self):
        return self[1]
    @x.setter
    def x(self, v):
        self[0] = v
    @y.setter
    def y(self, v):
        self[1] = v    
    
    def __call__(self):
        return Vector2D(self.x, self.y)
        
    def swap(self):
        return self(self.y, self.x)
    @property
    def sum(self):
        return self.x + self.y
    @property
    def product(self):
        return self.x * self.y
    @property
    def hypot(self):
        return (self ** 2).sum
    @property
    def length(self):
        return math.sqrt(self.hypot)
    @length.setter
    def length(self, length):
        self[:] = self.norm[:] * length
    @hypot.setter
    def hypot(self, hypot):
        self[:] = self.norm[:]
        self[:] *= math.sqrt(hypot)
    
    @property
    def angle(self):
        return math.atan2(self.y, self.x)
    @angle.setter
    def angle(self, angle):
        l = self.length
        self[:] = [math.cos(angle), math.sin(angle)]
        self *= l
    @property
    def norm(self):
        return self / self.length
    
    def gethypot(self, o):
        return (self - o).hypot
    def getdistance(self, o):
        return (self - o).length
    def dotproduct(self, o):
        return (self * o).sum
    
#     Angle addition formulae
    def sinAdd(self, other):
        return self.y * other[0] + self.x * other[1]
    def sinSub(self, other):
        return self.y * other[0] - self.x * other[1]
    def cosAdd(self, other):
        return self.x * other[0] - self.y * other[1]
    def cosSub(self, other):
        return self.x * other[0] + self.y * other[1]
    def angleAdd(self, other):
        return Vector2D(self.cosAdd(other), self.sinAdd(other))
    def angleSub(self, other):
        return Vector2D(self.cosSub(other), self.sinSub(other))