
'''
Created on Apr 20, 2015

@author: jacobrettig
'''
from library.vector2d import Vector2D


class Entity():
    def __init__(self, x, y):
        self.pos = Vector2D(x, y)