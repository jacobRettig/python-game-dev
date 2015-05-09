'''
Created on May 9, 2015

@author: lisarettig
'''

from vector2d import Vector2D
from collections import Iterable
import math

# quick get/set based on property class
# to avoid pointless @property&v.setter spam
class GS(object):
    def __init__(self, name, attr):
        self.name, self.attr = name, attr
        
    def __get__(self, inst, type=None):
        if inst is None:
            return self
        print("instance:{}".format(dir(inst)))
#         print("name:{}, val:{}".format(self.name), getattr(inst, self.name))
        return getattr(getattr(inst, self.name), self.attr)

    def __set__(self, inst, value):
        setattr(getattr(inst, self.name), self.attr, value)

    def __delete__(self, inst):
        return delattr(getattr(inst, self.name), self.attr)
    
    
    
# Will have a point relative to the owner's coords with a vertical and horizontal dilation multiplied by var 'side'
# owner = the instance calling method which holds referenced coords
# h = horizontal dilation factor
# v = vertical dilation factor
def refPoint(owner, h, v):
    class RefPoint(Vector2D):
#         get rid of normal Vector init stuff because RefPoint doesn't save instance variables other than it's local refs
        def __init__(self):
            pass
        
#         getters and setters for x&y
        @property
        def x(self):
            return owner.x + owner.side*h
        @x.setter
        def x(self, val):
            owner.x = val - owner.side*h
            
        @property
        def y(self):
            return owner.y + owner.side*v
        @y.setter
        def y(self, val):
            owner.y = val - owner.side*v
            
#         override normal Vector stuff to prevent unnecessary crashes
        def __len__(self):
            return 2
        
        def __getitem__(self, k):
            if k == 0 or k == 'x':
                return self.x
            elif k == 1 or k == 'y':
                return self.y
            else:
                raise IndexError
        def __setitem__(self, k, v):
            if k == 0 or k == 'x':
                self.x = v
            elif k == 1 or k == 'y':
                self.y = v
            else:
                raise IndexError

        @property
        def list(self):
            return [self.x, self.y]
        
        def __iter__(self):
            return self.list.__iter__()
        
#         remove reference and just use as a normal point
        def __call__(self):
            return Vector2D(self.x, self.y)    
#    return the class with it's local scope saved
    return RefPoint()


# prevent the deletion and overwriting of hidden Points instance instead of just replacing the hidden point's values 
class SafeSet(object):
#     name = name of hidden instance syntax '_{name}_'
    def __init__(self, name):
        self.name = name
        
#    access the hidden variable
    def __get__(self, inst, type=None):
        if inst is None:
            return self
        return getattr(inst, "_{}_".format(self.name))

#     instead of overwriting instance, just change internal values
    def __set__(self, inst, value):
        self.__get__(inst).x = value[0]
        self.__get__(inst).y = value[1]

#     disallow deletion
    def __delete__(self, inst):
        raise AttributeError("can't delete attribute")
    
# raised when geometric logic is broken
class InvalidGeometry(Exception):
    pass


# An axis-aligned square with coordinates
# data in key stored as [top left, top right, bottom right, bottom left]
class Square(Iterable):
#     data = (x, y, side length)
    def __init__(self, data = (0, 0, 0)):
#         init side length
        self._side_ = data[2]
        
#         init primary position reference location
        self.tl = Vector2D(data[0], data[1])
        
#         init all other points relative to top left
        self._tr_ = refPoint(self, 1, 0)
        self._bl_ = refPoint(self, 0, 1)
        self._br_ = refPoint(self, 1, 1)
        self._cen_ = refPoint(self, .5, .5)
        
        
#     this prevents overwriting instance variables
    tr = SafeSet('tr')
    bl = SafeSet('bl')
    br = SafeSet('br')
    cen = SafeSet('cen')
        
        
#     init quick get corner and center x&y values
    x = GS('tl', 'x')
    y = GS('tl', 'y')
    
    cx = GS('cen', 'x')
    cy = GS('cen', 'y')
    
    ox = GS('br', 'x')
    oy = GS('br', 'y')
        
        
#     specific to square

#     list of vertexes
    @property
    def list(self):
        return [self.tl, self.tr, self.br, self.bl]
    
    @property
    def area(self):
        return self.side ** 2
    @area.setter
    def area(self, newArea):
        self.side = math.sqrt(newArea)
        
    @property
    def perimeter(self):
        return 4 * self.side
    @perimeter.setter
    def perimeter(self, newPerimeter):
        self.side = newPerimeter / 4
        
    @property
    def normalProjection(self, point):
        x, y = 0, 0
        
        if self.ox > point.x:
            if self.x < point.x:
                x = 2
            else:
                x = 1
        if self.oy > point.y:
            if self.y < point.y:
                y = 2
            else:
                y = 1
                
        l, r = None, None
        if x == 0:
            if y == 0:
                l = self.bl
                r = self.tr
            elif y == 1:
                l = self.br
                r = self.tr
            else:
                l = self.br
                r = self.tl
        elif x == 1:
            if y == 0:
                l = self.bl
                r = self.br
            elif y == 1:
                raise InvalidGeometry("Point is Inside the Square")
            else:
                l = self.tr
                r = self.tl
        else:
            if y == 0:
                l = self.tl
                r = self.br
            elif y == 1:
                l = self.tl
                r = self.bl
            else:
                l = self.tr
                r = self.bl
        return [l, r]
    
#     assuming not inside
    def hypot(self, other):
        if isinstance(other, Square):
            return max(self.x - other.ox, other.x - self.ox, 0)**2 + max(self.y - other.oy, other.y - self.oy, 0)**2
        return max(self.x - other[0], other[0] - self.ox, 0)**2 + max(self.y - other[1], other[1] - self.oy, 0)**2
    
#     assuming not inside    
    def distance(self, other):
        return math.sqrt(self.hypot(other))
    
    
#     object behavior methods

    @property
    def side(self):
        return self._side_
    @side.setter
    def side(self, value):
        if value < 0:
            value = abs(value)
            self.tl -= value
        self._side_ = value
    
    def __str__(self):
        return "[x:{x}, y:{y}, side length:{side}]".format(x=self.x, y=self.y, side=self.side)
        
    def __eq__(self, other):
        if isinstance(other, Square):
           return other.x == self.x and other.y == self.y and other.side == self.side
        return False
    
    def __add__(self, other):
        sq = self()
        sq += other
        return sq
    
    def __sub__(self, other):
        sq = self()
        sq -= other
        return sq
        
    def __iadd__(self, other):
        self.tl += other
        return self
    
    def __isub__(self, other):
        self.tl -= other
        return self
    
    def __neg__(self, other):
        sq = self()
        sq.tl = sq.br - sq.tl
        return sq
        
    
#     get points to work with collection type stuff

    def __len__(self):
        return 4
    
    def __iter__(self):
        raise Exception("Squares are not Iterable")
    
    def __getitem__(self, key):
        if key == 0 or key == 'tl':
            return self.tl
        elif key == 1 or key == 'tr':
            return self.tr
        elif key == 2 or key == 'br':
            return self.br
        elif key == 3 or key == 'bl':
            return self.bl
        elif key == 'cen':
            return self.cen
        else:
            raise Exception
        
    def __setitem__(self, key, value):
        if key == 0 or key == 'tl':
            self.tl = value
        elif key == 1 or key == 'tr':
            self.tr = value
        elif key == 2 or key == 'br':
            self.br = value
        elif key == 3 or key == 'bl':
            self.bl = value
        elif key == 'cen':
            self.cen = value
        else:
            raise Exception
        
#     check if point or Square is inside of square (coordinate wise)
    def __contains__(self, value):
        if isinstance(value, Square):
#             check if primary point or opposite point is in other square (for both squares)
            return value.tl in self or value.br in self or self.tl in value or self.br in value
#         determine if point is inside square exclusive
        return value[0] > self.x and value[0] < self.ox and value[1] > self.y and value[1] < self.oy

#     clone self
    def __call__(self):
        return Square((self.x, self.y, self.side))
    
