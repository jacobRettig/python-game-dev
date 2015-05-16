'''
Created on May 9, 2015

@author: lisarettig
'''

from vector2d import Vector2D
from collections import Iterable
import math, util

    
    
# Will have a point relative to the owner's coords with a vertical and horizontal dilation multiplied by var 'side'
# owner = the instance calling method which holds referenced coords
# h = horizontal dilation factor
# v = vertical dilation factor
def refPoint(owner, h, v):
    class RefPoint(Vector2D, Iterable):
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
            if isinstance(k, slice):
                start = k.start
                if start is None:
                    start = 0
                stop = k.stop
                if stop is None:
                    stop = 1
                step = k.step
                if step is None:
                    step = 1
                for i in range(start, stop, step):
                    self[i] = v[i]
            elif k == 0 or k == 'x':
                self.x = v
            elif k == 1 or k == 'y':
                self.y = v
            else:
                raise IndexError('Square: {sq}  key: {k}  value: {v}'.format(sq=self, k=k, v=v))

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

# raised when geometric logic is broken
class InvalidGeometry(Exception):
    pass


# An axis-aligned square with coordinates
# data in key stored as [top left, top right, bottom right, bottom left]
class Square(Iterable):
#     data = (x, y, side length)
    def __init__(self, data = (0, 0, 0)):
#         init side length
        self.side = data[2]
        
#         init primary position reference location
        self._tl = Vector2D(data[0], data[1])
        
#         init all other points relative to top left
        self._tr = refPoint(self, 1, 0)
        self._bl = refPoint(self, 0, 1)
        self._br = refPoint(self, 1, 1)
        self._cen = refPoint(self, .5, .5)
        
        
#     this prevents overwriting instance variables
    @util.InstanceGuard('_tl', 'set')
    def tl(self, value):
        self.tl.x = value[0]
        self.tl.y = value[1]
    @util.InstanceGuard('_tr', 'set')
    def tr(self, value): 
        self.tr.x = value[0]
        self.tr.y = value[1]
    @util.InstanceGuard('_bl', 'set')
    def bl(self, value): 
        self.bl.x = value[0]
        self.bl.y = value[1]
    @util.InstanceGuard('_br', 'set')
    def br(self, value): 
        self.br.x = value[0]
        self.br.y = value[1]
    @util.InstanceGuard('_cen', 'set')
    def cen(self, value): 
        self.cen.x = value[0]
        self.cen.y = value[1]
        
        
#     init quick get corner and center x&y values
    x = util.GS('x', 'tl')
    y = util.GS('y', 'tl')
    
    cx = util.GS('x', 'cen')
    cy = util.GS('y', 'cen')
    
    ox = util.GS('x', 'br')
    oy = util.GS('y', 'br')
        
        
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
            return value.br in Square((self.x, self.y, self.side + value.side))
#         determine if point is inside square exclusive
        return value[0] > self.x and value[0] < self.ox and value[1] > self.y and value[1] < self.oy

#     clone self
    def __call__(self):
        return Square((self.x, self.y, self.side))
