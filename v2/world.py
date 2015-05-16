'''
Created on Apr 20, 2015

@author: jacobrettig
'''

import pygame

from player import Player
from map import Map as MapClass


class World():
    SIZE = 64
    
    def __init__(self, mapText, timeSpeed=1):
        self.timeSpeed = timeSpeed
        self.time = 0
        
        self.player = Player.DEFAULT(self)
        self.entityList = [self.player]
        self._map = MapClass(self, mapText)
        
    @property
    def map(self):
        return self._map
    
    @property
    def objectList(self):
        return self.entityList + self.map[:]
    
    def update(self):
        self.time += self.timeSpeed * self.player.timeRate()
        
        for entity in self.entityList:
            if entity.update():
                self.entityList.remove(entity)
        
        
        
