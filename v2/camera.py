import pygame
from vector2d import Vector2D

class Camera:
    def __init__(self, screen, background, pos, zoomScale, world):
        self.screen = screen
        self.background = background
        self.world = world

        self.pos = pos
        self.zoomScale = zoomScale

    def draw(self):
        gameMap = self.world.gameMap
        tileSheet = gameMap.
        entList = self.world.entityList

        mapTopLeft = self.pos / Vector2D(gameMap.cellWidth, gameMap.cellHeight)
        mapBotRight = (self.pos + (self.screen.get_width(), self.screen.get_height())) / Vector2D(gameMap.cellWidth, gameMap.cellHeight)        
        for tile in gameMap:
            curMapPos = mapTopLeft + tile.tl
            
            if curMapPos.hypot > mapTopLeft.hypot and curMapPos.hypot < mapBotRight.hypot:
                pass

        for entity in entList:
            pass # Draw each entity

        pygame.display.flip()
