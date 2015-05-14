'''
Created on Apr 20, 2015

@author: jacobrettig
'''

import pygame

from library.v2.player import Player
from map import Map as MapClass


class World():
    def __init__(self, screen, mapText, timeSpeed=1):
        self._screen, self._background = screen, pygame.Surface(screen.get_size())
        self._map = MapClass(self, mapText)
        
        self.background.fill((255, 255, 255))
        
        self.timeSpeed = timeSpeed
        self.time = 0
        self.entityList = []
        self.player = Player.DEFAULT(self)
        
    @property
    def map(self):
        return self._gameMap
    @property
    def screen(self):
        return self._screen
    @property
    def background(self):
        return self._background
    
    @property
    def objectList(self):
        return self.entityList + self.map.TileList
    
    def update(self):
        self.time += self.timeSpeed * self.player.timeRate()
        
        for entity in self.entityList:
            if entity.update():
                self.entityList.remove(entity)
        
        
        
