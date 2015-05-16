import pygame
from vector2d import Vector2D
import tile
import entity
from square import Square

class Camera:
    CELLSIZE = 32
    
    def __init__(self, background, world, pos=None, zoom=1):
        self.background = background
        self.world = world
        if pos is None:
            pos = (0, 0)
        self.pos = Vector2D(pos[0], pos[1])
        self.zoom = zoom

#     screen must be a square Surface
    def draw(self, screen):
        if screen.get_width() != screen.get_height():
            raise Exception('Must pass in square screen')
#         
#         display.cen += self.world.player.cen + self.pos
#         display.side = screen.get_width()
        gameSpace = Square((0, 0, self.world.map.width))
#         gameSpace.side /= self.CELLSIZE
        
        
        
#         screenSize = Vector2D(screen.get_width(), screen.get_height()) / (2 * self.CELLSIZE)
#         pos = self.world.player.cen
#         if self.pos is not None:
#             pos += self.pos
# 
#         gameMap = self.world.map
#         entList = self.world.entityList

#         mapTopLeft = self.pos - screenSize
#         mapBotRight = self.pos + screenSize
        
#         tileList = []
        for tile in self.world.map[:]:
#             curMapPos = mapTopLeft + tile.tl
            screen.blit(tile.image, tuple((tile.tl) * 32))
#             tileList.append(tile)
#             screenPos = curMapPos * self.CELLSIZE - self.pos
#             screen.blit(tile.image, (screenPos.x, screenPos.y))

#         fn = (lambda x, y: x.oy - y.oy)
        
        for E in (E2 for E2 in self.world.entityList if E2 in gameSpace):
            image = E.image
            width, height = image.get_width(), image.get_height()
            screen.blit(image, E.tl)

#         drawList = util.binaryInsertionSort(fn, drawList, entList)
#         for obj in drawList:
#             if isinstance(obj, tile.Tile):
#                 screen.blit(obj.image, tuple((cmapTopLeft + tile.tl) * self.CELLSIZE - self.pos))
#             elif isinstance(obj, entity.Entity):
#             screen.blit(entity.image, entity.imagePosition)
        



