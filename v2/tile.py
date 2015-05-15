'''
Created on May 12, 2015

@author: jacobrettig
'''

import pygame

from gameObject import GameObject

def loadTerrain(path, width, height):
    img = pygame.image.load(path)
    images = [None] * width
    for i in range(width):
        images[i] = [None] * height
        for j in range(height):
            images[i][j] = img.subsurface((i * img.get_width() / width, j * img.get_height() / height, img.get_width() / width, img.get_height() / height))
    return images


class Tile(GameObject):
    images = loadTerrain('terrain/terrain_atlas.png', 32, 32) 
    
    def __init__(self, world, val, x, y):
        GameObject.__init__(self, world, (x, y, 1))
        if val in ' PN':
            self.id = ' '
        elif val in '#':
            self.id = '#'
            self.isOpque = True
            self.isSolid = True
        
    @property
    def image(self):
        if self.id is ' ':
            return self.images[30][10]
        elif self.id is '#':
            try:
                if self.world.map[self.tl + (0, 1)].id is '#':
                    return self.images[25][11]
            except IndexError:
                pass
            return self.images[24][7]












