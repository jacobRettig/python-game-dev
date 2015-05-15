import pygame
from vector2d import Vector2D


class Camera:
    CELLSIZE = 32
    
    def __init__(self, background, world, pos=None, zoom=1):
        self.background = background
        self.world = world
        self.pos = Vector2D(pos)
        self.zoom = zoom

    def draw(self, screen):
        screenSize = Vector2D(screen.get_width(), screen.get_height()) / (2 * self.CELLSIZE)
        pos = self.pos
        if pos is None:
            pos = self.world.player.cen

        gameMap = self.world.map
        entList = self.world.entityList

        mapTopLeft = self.pos - screenSize
        mapBotRight = self.pos + screenSize
        
        for tile in gameMap.getTileRange(mapTopLeft, mapBotRight):
            curMapPos = mapTopLeft + tile.tl

            screenPos = curMapPos * self.CELLSIZE - self.pos
            screen.blit(tile.image, (screenPos.x, screenPos.y)) 

        for entity in entList:
            screen.blit(entity.image, entity.imagePosition)
        



