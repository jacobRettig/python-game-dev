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
    
    def _get_sightHypot(self):
        return self._sightHypot_
    def _set_sightHypot(self, v):
        self.sightDistance = math.sqrt(v)    
    def _get_sightDistance(self):
        return self._sightDistance_
    def _set_sightDistance(self, v):
        self._sightDistance_ = v
        self._sightHypot = v ** 2
        
    def _get_sightSpread(self):
        return self._sightSpread_
    def _set_sightSpread(self, v):
        self._sightCos_ = math.cos(v)
        self._sightSin_ = math.sin(v)
        self._sightSpread_ = v
    
    def _get_sightCos(self):
        return self._sightCos_
    def _set_sightCos(self, v):
        raise AttributeError
    def _get_sightSin(self):
        return self._sightSin_
    def _set_sightSin(self, v):
        raise AttributeError
    
        
        
        
        