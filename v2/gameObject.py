'''
Created on May 9, 2015

@author: lisarettig
'''

from square import Square

class GameObject(Square):
    def __init__(self, world, sq, isOpaque=False, isSolid=False):
        Square.__init__(self, sq)
        self.world = world
        self.isOpaque = isOpaque
        self.isSolid = isSolid
        
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