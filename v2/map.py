'''
Created on Apr 27, 2015

@authand: jacobrettig
'''
from collections import Iterable
import functools
from numbers import Number
from random import Random

from pygame.examples.moveit import GameObject

from gameObject import GameObject
from square import Square
from tile import Tile
from vector2d import Vector2D


rand = Random()

    
class Map(Square):
    def __init__(self, world, text):
        self.world = world
        self.text = text
        side = (min(functools.reduce(min, list(map(len, text))), len(text)) - 1)
        Square.__init__(self, (0, 0, self.world.SIZE * side))
        self.data = {}
        
        for i in range(side):
            for j in range(side):
                self.data[str((i, j))] = Tile(self.world, self.text[i][j], i, j)
                
        self.completeSet = frozenset(self.data.values())
        
        self.solidTiles = set()
        self.opaqueTiles = set()
        for tile in self[:]:
            if tile.isSolid:
                self.solidTiles.add(tile)
            if tile.isOpaque:
                self.opaqueTiles.add(tile)
        self.completeSet = frozenset(self.data.values())
        self.solidTiles = frozenset(self.solidTiles)
        self.openTiles = tuple(self.completeSet - self.solidTiles)
        self.opaqueTiles = frozenset(self.opaqueTiles)
        
    def __len__(self):
        return (self.side / self.world.SIZE, self.side / self.world.SIZE)
    
    def __getitem__(self, k):
        if isinstance(k, slice):
            if k.start == None and k.stop == None:
                return self.completeSet
            
            start = k.start
            if not isinstance(start, Iterable):
                start = (self._tl[0], self._tl[1])
            
            stop = k.stop
            if not isinstance(stop, Iterable):
                stop = (self._br.x, self._br.y)
            
            tlx = min(start[0], stop[0])
            tly = min(start[1], stop[1])
            brx = max(start[0], stop[0])
            bry = max(start[1], stop[1])
            results = set()
            
            for tile in self.completeSet:
                if tlx - tile.side <= tile._tl[0] <= brx and tly - tile.side <= tile._tl[1] <= bry:
                    results.add(tile)
                     
            return results
            
        elif len(k) == 2:
            return self.data[str((int(max(min(k[0], self.side - self.world.SIZE), 0) // self.world.SIZE),
                 int(max(min(k[1], self.side - self.world.SIZE), 0) // self.world.SIZE)))]
        raise IndexError(k, type(k))
    
    def __setitem__(self, k, v):
        raise AttributeError
    
        
    
    
