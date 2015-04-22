
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from base import Base
from vector2d import Vector2D


class Entity(Base):
    def __init__(self, world, x, y, width, height, image = None):
        self.world = world
        self.pos = Vector2D(x, y)
        self._width_, self._height_, width, height
        self._image_ = image
        self._animation_ = None
        self._dx_, self._dy_ = None, None
        
    def _get_width(self):
        return self._width_
    def _set_width(self, v):
        raise AttributeError
    def _get_w(self):
        return self._width_
    def _set_w(self, v):
        raise AttributeError

    def _get_height(self):
        return self._height_
    def _set_height(self, v):
        raise AttributeError
    def _get_h(self):
        return self._height_
    def _set_h(self, v):
        raise AttributeError
    
    def __getitem__(self, k):
        return self.pos.__getitem__(k)
    def __setitem__(self, k, v):
        return self.pos.__setitem__(k, v)
    
    def _get_x(self):
        return self.pos.x
    def _set_x(self, v):
        self.pos.x = v
    def _get_left(self):
        return self.pos.x
    def _set_left(self, l):
        self.pos.x = l
    def _get_l(self):
        return self.pos.x
    def _set_l(self, l):
        self.pos.x = l
    
    def _get_y(self):
        return self.pos.y
    def _set_y(self, y):
        self.pos.y = y
    def _get_top(self):
        return self.pos.y
    def _set_top(self, y):
        self.pos.y = y
    def _get_t(self):
        return self.pos.y
    def _set_t(self, y):
        self.pos.y = y
        
    def _get_right(self):
        return self.pos.x + self.w
    def _set_right(self, v):
        self.pos.x = v - self.w
    def _get_r(self):
        return self.pos.x + self.w
    def _set_r(self, v):
        self.pos.x = v - self.w
        
    def _get_bottom(self):
        return self.pos.y + self.h
    def _set_bottom(self, v):
        self.pos.y = v - self.h
    def _get_b(self):
        return self.pos.y + self.h
    def _set_b(self, v):
        self.pos.y = v - self.h
        
    def isInside(self, other):
        if isinstance(other, Entity):
            return other.r >= self.l and other.b >= self.t and other.l <= self.r and other.t <= self.b
        elif isinstance(other, Vector2D):
            return other.x >= self.l and other.x <= self.r and other.y >= self.t and other.y <= self.b
        else:
            raise AttributeError
        
    def _get_dx(self):
        return self._dx_
    def _set_dx(self, v):
        self._dx_ = v

    def _get_dy(self):
        return self._dy_
    def _set_dy(self, v):
        self._dy_ = v
            
    def _get_image(self):
        return self._image_
    def _set_image(self, v):
        self._image_ = v
    
    def _get_animation(self):
        return self._animation_
    def _set_animation(self, v):
        self._animation_ = v
    
    def update(self):
        pass
    
    