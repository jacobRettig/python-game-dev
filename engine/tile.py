'''
Created on May 12, 2015

@author: jacobrettig
'''

import pygame
from engine.gameObject import GameObject

def loadTerrain(path, width, height):
    img = pygame.image.load('engine/' + path)
    img = pygame.transform.scale2x(img)
    images = [None] * width
    for i in range(width):
        images[i] = [None] * height
        for j in range(height):
            images[i][j] = img.subsurface((i * img.get_width() / width, j * img.get_height() / height, img.get_width() / width, img.get_height() / height))
    return images


class Tile(GameObject):
    images = loadTerrain('terrain/terrain_atlas.png', 32, 32) 
    
    def __init__(self, world, val, x, y):
        GameObject.__init__(self, world, (x * world.SIZE, y * world.SIZE, world.SIZE))
        if val in ' PN':
            self._id = ' '
        elif val in '#':
            self._id = '#'
            self.isOpque = True
            self.isSolid = True
        else:
            raise TypeError('invaild value: {v}'.format(v=val))
        
    def __hash__(self):
        return id(self)
    
    @property
    def image(self):
        if self._id == ' ':
            return self.images[30][10]
        elif self._id == '#':
            if self.oy != self.world.map.oy and self.world.map[self._tl + (0, self.world.SIZE)]._id == '#':
                return self.images[25][11]
            else:
                return self.images[24][7]
        else:
            print('problem loading image from tile id : {id}'.format(id=self._id))












