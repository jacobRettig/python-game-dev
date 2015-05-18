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
        
        from spriteSheetLPC import LPC
        self.spriteSheet = LPC(body='skeleton')
        
    @property
    def map(self):
        return self._map
    
    def update(self):
        self.time += self.timeSpeed * self.player.timeRate()
        removalSet = set()
        for entity in self.entityList:
            if entity.update():
                removalSet.add(entity)
        self.entityList.difference_update(removalSet)
        
    def addEnemy(self):
        E = Enemy(self, (0, 0, World.SIZE/2), self.spriteSheet)
        E.speed = 1.5
        import random
        while True:
            E.cx = random.random() * self.map.side
            E.cy = random.random() * self.map.side
            E.keepInside(self.map)
            for tile in self.map.solidTiles:
                if E in tile:
                    continue
            break
        E.target = E.cen
        self.entityList.add(E)
        
        