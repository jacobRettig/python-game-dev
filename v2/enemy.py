'''
Created on Apr 29, 2015

@author: jacobrettig
'''

import math

from base import Base
from entity import Entity


class Enemy(Entity):
    def __init__(self, world, x, y, width, height, sightDistance, sightSpread, hp = 30, image = None):
        Entity.__init__(self, world, x, y, width, height, image)
        self.hp, self.sightDistance, self.sightSpread = hp, sightDistance, sightSpread
    
    @property
    def sightHypot(self):
        return self._sightHypot_
    @sightHypot.setter
    def sightHypot(self, v):
        self.sightDistance = math.sqrt(v)
    @property    
    def sightDistance(self):
        return self._sightDistance_
    @sightDistance.setter
    def sightDistance(self, v):
        self._sightDistance_ = v
        self._sightHypot = v ** 2
        
    @property
    def sightSpread(self):
        return self._sightSpread_
    @sightSpread.property
    def sightSpread(self, v):
        self._sightCos_ = math.cos(v)
        self._sightSin_ = math.sin(v)
        self._sightSpread_ = v
    
    @property
    def sightCos(self):
        return self._sightCos_
    @sightCos.getter
    def sightCos(self, v):
        raise AttributeError
    @property
    def sightSin(self):
        return self._sightSin_
    @sightSin.getter
    def sightSin(self, v):
        raise AttributeError
    
        
        
        
        