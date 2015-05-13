'''
Created on May 12, 2015

@author: jacobrettig
'''

from gameObject import GameObject

class TileConstant():
    def __init__(self, **kwargs):
        self.isOpaque = False
        self.isCollidable = False
        self.action = None
        self.posX = None
        self.posY = None
        for key in ('isOpaque', 'isCollidable', 'action', 'imageFn'):
            if key in kwargs:
                setattr(self, key, kwargs.pop(key))
        if len(kwargs) != 0:
            raise Exception('left over kwargs : {}'.format(kwargs))
    
    def actionFn(self, viewer):
        if not self.action is None:
            return self.action(self, viewer)
    
    def actionSetter(self, fn):
        self.action = fn
        return self
        
    def imageFn(self):
        if not self.action is None:
            return self.action(self)
    
    def imageFnSetter(self, fn):
        self.imageFn = fn
        return self
    
    
    def getAdjacent(self, xDiff, yDiff):
        raise Exception("not yet implemented")
    
    @property
    def image(self):
        return self.imageFn()
    




GRASS = TileConstant()
@GRASS.imageFnSetter
def GRASS(self):
    















