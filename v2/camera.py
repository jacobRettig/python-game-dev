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
        
        display = Square((0, 0, screen.get_width()))
        display.side /= self.zoom
        display.cen = self.world.player.cen()
        display.keepInside(self.world.map)
        print(self.world.map.br)
        
        for tile in self.world.map[display.tl : display.br]:
            screen.blit(tile.image, tile.tl - display.tl)
        
        for E in self.world.entityList:#(E2 for E2 in self.world.entityList if E2 in gameSpace):
            pnt = Vector2D(E.cx, E.oy) - (E.image.get_width() / 2, E.image.get_height())
            
            screen.blit(E.image, pnt - display.tl)

        



