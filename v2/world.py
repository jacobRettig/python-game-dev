'''
Created on Apr 20, 2015

@author: jacobrettig
'''

import pygame

from player import Player
from map import Map as MapClass
from enemy import Enemy


class World():
    SIZE = 64
    
    def __init__(self, mapText, timeSpeed=1):
        self.timeSpeed = timeSpeed
        self.time = 0
        
        self.player = Player.DEFAULT(self)
        self.entityList = [self.player]
        self._map = MapClass(self, mapText)
        
        from spriteSheetLPC import LPC
        self.spriteSheet = LPC(body='skeleton')
        
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
        self.entityList.append(E)
        
