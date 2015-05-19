'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from enemy import Enemy
from map import Map as MapClass
from player import Player


class World():
    SIZE = 64
    
    def __init__(self, mapText, timeSpeed=1):
        self.timeSpeed = timeSpeed
        self.time = 0
        
        self.player = Player.DEFAULT(self)
        self.entityList = set((self.player, ))
        self._map = MapClass(self, mapText)
        
        self.loadedSheets = {}
        
    @property
    def map(self):
        return self._map
    
    def update(self):
        self.time += self.timeSpeed * self.player.timeRate()
        removalSet = set()
        for entity in self.entityList:
            entity.update()
            if not entity.isAlive:
                removalSet.add(entity)
        self.entityList.difference_update(removalSet)
        
    
        
        