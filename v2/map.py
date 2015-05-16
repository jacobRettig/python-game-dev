'''
Created on Apr 27, 2015

@authand: jacobrettig
'''
from collections import Iterable
from random import Random

from vector2d import Vector2D
from square import Square
from tile import Tile
from numbers import Number
from pygame.examples.moveit import GameObject
from gameObject import GameObject


rand = Random()

    
class Map(Square):
    def __init__(self, world, text):
        self.world = world
        self.text = text
        Square.__init__(self, (0, 0, self.world.SIZE * (min(reduce(min, list(map(len, text))), len(text)) - 1)))
        self.data = {}
        self.empty = self.side ** 2
        self._solidTiles = tuple()
        self._opaqueTiles = tuple()
        for tile in self[:]:
            if tile.isSolid:
                self._solidTiles += (tile, )
            if tile.isOpaque:
                self._opaqueTiles += (tile, )
        
    @property
    def unloadedCount(self):
        return self.empty
    
    @property
    def solidTiles(self):
        return self._solidTiles
    
    @property
    def opaqueTiles(self):
        return self._opaqueTiles
    
    def __len__(self):
        return (self.side, self.side)
    
    def __getitem__(self, k):
        if isinstance(k, slice):
            start = k.start
            if start is None or not isinstance(start, Iterable):
                start = (self._tl[0], self._tl[1])
            
            stop = k.stop
            if stop is None or not isinstance(stop, Iterable):
                stop = (self._br.x, self._br.y)
            
            tlx = min(start[0], stop[0])
            tly = min(start[1], stop[1])
            brx = max(start[0], stop[0]) + self.world.SIZE
            bry = max(start[1], stop[1]) + self.world.SIZE
            x = tlx
            y = tly
            results = tuple()
            while y < bry:
                while x < brx:
                    results += (self[(x, y)], )
                    x += self.world.SIZE
                x = tlx
                y += self.world.SIZE
            return results
            
        elif isinstance(k, Iterable) and len(k) == 2:
            k = Vector2D(*k).map(max, 0).map(min, self.side - self.world.SIZE)
            k = (int(max(min(k[0], self.side - self.world.SIZE), 0) // self.world.SIZE),
                 int(max(min(k[1], self.side - self.world.SIZE), 0) // self.world.SIZE))
            strk = str(k)
            if strk not in self.data:
                self.data[strk] = Tile(self.world, self.text[k[1]][k[0]], k[0], k[1])
                self.empty -= 1
            return self.data[strk]
        raise IndexError(k, type(k))
    
    def __setitem__(self, k, v):
        raise AttributeError
    
        
    
    
