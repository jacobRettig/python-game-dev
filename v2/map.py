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
        
    @property
    def unloadedCount(self):
        return self.empty
    
    def __len__(self):
        return (self.side, self.side)
    
    def __getitem__(self, k):
        if isinstance(k, slice):
            start = k.start
            if start is None or isinstance(start, Number):
                start = self.tl
            start = Vector2D(start[0], start[1])
            
            stop = k.stop
            if stop is None or isinstance(stop, Number):
                stop = self.br
            stop = Vector2D(stop[0], stop[1])
            
            tl = Vector2D(min(start.x, stop.x), min(start.y, stop.y))
            br = Vector2D(max(start.x, stop.x), max(start.y, stop.y))
            
            indexer = tl()
            results = []
            while indexer.y < br.y + self.world.SIZE:
                while indexer.x < br.x + self.world.SIZE:
                    results.append(self[indexer])
                    indexer.x += self.world.SIZE
                indexer.x = tl.x
                indexer.y += self.world.SIZE
            return results
            
        elif (isinstance(k, Iterable) or isinstance(k, tuple)) and len(k) == 2:
            k = Vector2D(*k).map(max, 0).map(min, self.side - self.world.SIZE)
            k //= self.world.SIZE
            k = k.map(int)
            if str(k) not in self.data:
                self.data[str(k)] = Tile(self.world, self.text[k[1]][k[0]], k[0], k[1])
                self.empty -= 1
#             print('accessing tile with : {}   val : {}'.format(k, self.data[str(k)]))
            return self.data[str(k)]
        raise IndexError(k, type(k))
    
    def __setitem__(self, k, v):
        raise AttributeError
    
        
    
    
