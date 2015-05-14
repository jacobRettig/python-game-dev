'''
Created on May 12, 2015

@author: jacobrettig
'''

import pygame

from gameObject import GameObject

def loadTerrain(path, width, height):
    img = pygame.image.load(path)
    images = []
    for i in range(width):
        images[i] = []
        for j in range(height):
            images[i][j] = img.subsurface((i * img.get_width() / width, j * img.get_height() / height, img.get_width() / width, img.get_height() / height))
    return images


class Tile(GameObject):
    images = loadTerrain('terrain/terrain_atlas.png', 32, 32) 
    
    def __init__(self, world, val, x, y):
        GameObject.__init__(self, world, (x, y, 1))
        if val in ' P':
            self._image = self.images[30][10]
        elif val in 'N#':
            self.image = self.images[24][7]
            self.isOpque = True
            self.isSolid = True
        
    @property
    def image(self):
        return self._image













