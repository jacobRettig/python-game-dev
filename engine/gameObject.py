'''
Created on May 9, 2015

@author: lisarettig
'''

from engine.square import Square

class GameObject(Square):
    def __init__(self, world, sq, isOpaque=False, isSolid=False):
        Square.__init__(self, sq)
        self.world = world
        self.isOpaque = isOpaque
        self.isSolid = isSolid
        
    def __hash__(self):
        return id(self)    
    
    @property
    def image(self):
        raise AttributeError("No Image Getter Defined")
    @image.setter
    def image(self, value):
        raise AttributeError("No Image Setter Defined")
    @image.deleter
    def image(self):
        raise AttributeError("No Image Getter Defined")
    
#    if returns True then delete the Instance
    def update(self):
        False