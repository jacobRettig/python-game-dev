import pygame

import entity
from square import Square
import tile


class Camera:
    CELLSIZE = 32
    if pygame.font.get_init() == False:
        pygame.font.init()
        
    def __init__(self, background, world, zoom=1):
        self.background = background
        self.world = world
        self.zoom = zoom

#     screen must be a square Surface
    def draw(self, screen):
        display = Square((0, 0, min(screen.get_width(), screen.get_height())))
        display.side /= self.zoom
        screen.set_clip((0, 0, display.side, display.side))
        display.cen = self.world.player.cen()
        display.keepInside(self.world.map)

        self.drawMap(screen, display)
        
        for E in self.world.entityList:
            if E in display:
                screen.blit(E.image, E.imagePosition - display.tl)
                
        for E in self.world.entityList:
            if E in display and E.blurb != None:
                font = pygame.font.Font(pygame.font.get_default_font(), 20)
                text = font.render(E.blurb, False, (0, 0, 0))
                screen.blit(text, E.imagePosition - display.tl - (text.get_width() / 2, text.get_height()))
                
    def drawMap(self, screen, display):
        for tile in self.world.map.completeSet:
            if tile in display:
                screen.blit(tile.image, tile.tl - display.tl)
        

        



