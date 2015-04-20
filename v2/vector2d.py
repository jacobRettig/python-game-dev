'''
Created on Apr 20, 2015

@author: jacobrettig
'''

import math

from vector import Vector


class Vector2D(Vector):
    def __init__(self, x=0, y=0):
        Vector.__init__(self, x, y)
    
    def _get_x(self):
        return self[0]
    def _get_y(self):
        return self[1]
    def _set_x(self, v):
        self[0] = v
    def _set_y(self, v):
        self[1] = v    
    
    def __call__(self):
        return Vector2D(self.x, self.y)
        
    def swap(self):
        return self(self.y, self.x)
    
    def _get_sum(self):
        return self.x + self.y
    def _get_product(self):
        return self.x * self.y
    def _get_hypot(self):
        return (self ** 2).sum
    def _get_length(self):
        return math.sqrt(self.hypot)
    def _set_length(self, length):
        self[:] = self.norm[:] * length
    def _set_hypot(self, hypot):
        self[:] = self.norm[:]
        self[:] *= math.sqrt(hypot)
    
    def _get_angle(self):
        return math.atan2(self.y, self.x)
    def _set_angle(self, angle):
        l = self.length
        self[:] = [math.cos(angle), math.sin(angle)]
        self *= l
    def _get_norm(self):
        return self / self.length
        
    def gethypot(self, o):
        return (self - o).hypot
    def getdistance(self, o):
        return (self - o).length
    def dotproduct(self, o):
        return (self * o).sum
    
    
v = Vector2D(1, 2)
w = Vector2D(1, 1)
v.hypot = 6
print(v.hypot)