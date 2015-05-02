
'''
Created on Apr 20, 2015

@author: jacobrettig
'''

from vector2d import Vector2D


class Entity():
    def __init__(self, world, x, y, width, height, image = None):
        self.world = world
        self.pos = Vector2D(x, y)
        self._width_, self._height_, width, height
        self._image_ = image
        self._animation_ = None
        self._dx_, self._dy_ = None, None
        
    @property
    def width(self):
        return self._width_
    @width.setter
    def width(self, v):
        raise AttributeError
    @property
    def w(self):
        return self._width_
    @w.setter
    def w(self, v):
        raise AttributeError

    @property
    def height(self):
        return self._height_
    @height.setter
    def height(self, v):
        raise AttributeError
    @property
    def h(self):
        return self._height_
    @h.setter
    def h(self, v):
        raise AttributeError
    
    def __getitem__(self, k):
        return self.pos.__getitem__(k)
    def __setitem__(self, k, v):
        return self.pos.__setitem__(k, v)
    
    @property
    def x(self):
        return self.pos.x
    @x.setter
    def x(self, v):
        self.pos.x = v
    @property
    def left(self):
        return self.pos.x
    @left.setter
    def left(self, l):
        self.pos.x = l
    @property
    def l(self):
        return self.pos.x
    @l.setter
    def l(self, l):
        self.pos.x = l
    
    @property
    def y(self):
        return self.pos.y
    @y.setter
    def y(self, y):
        self.pos.y = y
    @property
    def top(self):
        return self.pos.y
    @top.setter
    def top(self, y):
        self.pos.y = y
    @property
    def t(self):
        return self.pos.y
    @t.setter
    def t(self, y):
        self.pos.y = y
        
    @property
    def right(self):
        return self.pos.x + self.w
    @right.setter
    def right(self, v):
        self.pos.x = v - self.w
    @property
    def r(self):
        return self.pos.x + self.w
    @r.setter
    def r(self, v):
        self.pos.x = v - self.w
        
    @property
    def bottom(self):
        return self.pos.y + self.h
    @bottom.setter
    def bottom(self, v):
        self.pos.y = v - self.h
    @property
    def b(self):
        return self.pos.y + self.h
    @b.setter
    def b(self, v):
        self.pos.y = v - self.h
        
    def isInside(self, other):
        if isinstance(other, Entity):
            return other.r >= self.l and other.b >= self.t and other.l <= self.r and other.t <= self.b
        elif isinstance(other, Vector2D):
            return other.x >= self.l and other.x <= self.r and other.y >= self.t and other.y <= self.b
        else:
            raise AttributeError
        
    @property
    def dx(self):
        return self._dx_
    @dx.setter
    def dx(self, v):
        self._dx_ = v

    @property
    def dy(self):
        return self._dy_
    @dy.setter
    def dy(self, v):
        self._dy_ = v
        
    @property    
    def image(self):
        return self._image_
    @image.setter
    def image(self, v):
        self._image_ = v
    
    @property
    def animation(self):
        return self._animation_
    @animation.setter
    def animation(self, v):
        self._animation_ = v
        
    def destroy(self):
        self.owner.entityList.remove(self)
        
    #TODO
    def update(self):
        return False
    def draw(self):
        pass
    
    