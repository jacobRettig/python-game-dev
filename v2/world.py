'''
Created on Apr 20, 2015

@author: jacobrettig
'''

import pygame

from base import Base

class World(Base):
    def __init__(self, screen, gameMap, timeSpeed=1):
        self._gameMap_, self._screen_, self._background_ = gameMap, screen, pygame.Surface(screen.get_size())
        
        self.background.fill((255, 255, 255))
        
        self.timeSpeed = timeSpeed
        self.time = 0
        self.entityList = []
        
    @property
    def gameMap(self):
        return self._gameMap_
    @gameMap.setter
    def gameMap(self, v):
        raise AttributeError
    @property
    def screen(self):
        return self._screen_
    @screen.setter
    def screen(self, v):
        raise AttributeError
    @property
    def background(self):
        return self._background_
    @background.setter
    def background(self, v):
        raise AttributeError
    
	# Jacob, the Camera class will handle drawing
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.gameMap.draw(self)
        
        for entity in self.entityList:
            entity.draw()
        
        pygame.display.flip()
        
    def update(self):
        self.time += self.timeSpeed
        
        for entity in self.entityList:
            entity.update()
        
        
        
