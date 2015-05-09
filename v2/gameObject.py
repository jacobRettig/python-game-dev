'''
Created on May 9, 2015

@author: lisarettig
'''

from square import Square

class GameObject(Square):
    def __init__(self, world, sq, isOpque=False):
        Square.__init__(self, sq)
        self.world = world
        self.isOpque = isOpque
        
    @property
    def image(self):
        raise AttributeError("No Image Getter Defined")
    @image.setter
    def image(self, value):
        raise AttributeError("No Image Setter Defined")
    @image.deleter
    def image(self):
        raise AttributeError("No Image Getter Defined")
    
    def update(self):
        pass