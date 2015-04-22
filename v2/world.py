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
        
    def _get_gameMap(self):
        return self._gameMap_
    def _set_gameMap(self, v):
        raise AttributeError
    def _get_screen(self):
        return self._screen_
    def _set_screen(self, v):
        raise AttributeError
    def _get_background(self):
        return self._background_
    def _set_background(self, v):
        raise AttributeError
    
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
        
        
        