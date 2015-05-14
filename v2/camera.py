import pygame
from vector2d import Vector2D

CELLSIZE = 32

class Camera:
    def __init__(self, background, pos, zoomScale, world):
        self.background = background
        self.world = world

        self.pos = pos
        self.zoomScale = zoomScale

    def draw(self, screen):
        screenSize = Vector2D(screen.get_width(), screen.get_height())

        gameMap = self.world.gameMap
        entList = self.world.entityList

        mapTopLeft = self.pos / CELLSIZE
        mapBotRight = (self.pos + screenSize) / CELLSIZE

        for tile in gameMap.getTileRange(mapTopLeft, mapBotRight):
            curMapPos = mapTopLeft + tile.tl

            screenPos = curMapPos * CELLSIZE - self.pos
            screen.blit(tile.image, (screenPos.x, screenPos.y)) 

        for entity in entList:
            pass # Draw each entity




