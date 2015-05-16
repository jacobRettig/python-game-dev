'''
Created on Apr 20, 2015

@author: jacobrettig
'''
from collections import Mapping, Iterable
import math, functools


class Vector(Iterable):
#     args = values included inside vector
    def __init__(self, *args):
        self.size = len(args)
        self.dat = [0] * len(self)
        self.dat[:] = args[:]
        
    TAU = math.pi * 2
    
    def __repr__(self):
        return self.__str__();

    def __str__(self):
        return "[< " + self.reduce((lambda x, y: str(x) + ", " + str(y))) + " >]"
    
    def __len__(self):
        return self.size
    
#     clone self
    def __call__(self):
        return Vector(*self)
    
    def map(self, fn, *args):
        self[:] = list(map(fn, self, *self.prep(*args)))
        return self
        
    def reduce(self, fn, *args):
        return functools.reduce(fn, self, *args)
        
#     prep val(s) as an iterable so map can use it
    def prep(self, *args):
        result = [0] * len(args) 
        for i in range(len(args)):
            if isinstance(args[i], Iterable):
                result[i] = args[i]
            else:
                result[i] = [args[i]] * len(self)
        return result
    
    def __getitem__(self, k):
        return self.dat.__getitem__(k)
    def __setitem__(self, k, v):
        return self.dat.__setitem__(k, v)
    def __iter__(self):
        return self.dat.__iter__()
    
#     operations
    def __add__(self, o):
        return self().map((lambda x, y: x + y), o)
    def __radd__(self, o):
        return self().map((lambda x, y: y + x), o)
    def __iadd__(self, o):
        return self.map((lambda x, y: x + y), o)
        
    def __sub__(self, o):
        return self().map((lambda x, y: x - y), o)
    def __rsub__(self, o):
        return self().map((lambda x, y: y - x), o)
    def __isub__(self, o):
        return self.map((lambda x, y: x - y), o)
        
    def __mul__(self, o):
        return self().map((lambda x, y: x * y), o)
    def __rmul__(self, o):
        return self().map((lambda x, y: y * x), o)
    def __imul__(self, o):
        return self.map((lambda x, y: x * y), o)
        
    def __div__(self, o):
        return self().map((lambda x, y: x / y), o)
    def __rdiv__(self, o):
        return self().map((lambda x, y: y / x), o)
    def __idiv__(self, o):
        return self.map((lambda x, y: x / y), o)
        
    def __truediv__(self, o):
        return self().map((lambda x, y: x / y), o)
    def __rtruediv__(self, o):
        return self().map((lambda x, y: y / x), o)
    def __itruediv__(self, o):
        return self.map((lambda x, y: x / y), o)
    
    def __floordiv__(self, o):
        return self().map((lambda x, y: x // y), o)
    def __rfloordiv__(self, o):
        return self().map((lambda x, y: y // x), o)
    def __ifloordiv__(self, o):
        return self.map((lambda x, y: x // y), o)
    
    def __mod__(self, o):
        return self().map((lambda x, y: x % y), o)
    def __rmod__(self, o):
        return self().map((lambda x , y: y % x), o)
    def __imod__(self, o):
        return self.map((lambda x, y: x % y), o)
        
    def __pow__(self, o):
        return self().map((lambda x, y: x ** y), o)
    def __rpow__(self, o):
        return self().map((lambda x, y: y ** x), o)
    def __ipow__(self, o):
        return self.map((lambda x, y: x ** y), o)
        
    def __abs__(self):
        return self().map((lambda x: abs(x)))
    def __pos__(self):
        return self().map((lambda x: +x))
    def __neg__(self):
        return self().map((lambda x: -x))
        
#     shift elements to left [0, 1, 2, 3] -> [1, 2, 3, 0]
    def __lshift__(self, o):
        if isinstance(o, int):
            v = self()
            v[:] = v[o % len(v):] + v[:o % len(v)]
            return v
        raise TypeError
#     shift elements to right [0, 1, 2, 3] -> [3, 0, 1, 2]
    def __rshift__(self, o):
        if isinstance(o, int):
            v = self()
            v[:] = v[-o % len(v):] + v[:-o % len(v)]
            return v
        raise TypeError
    
#     swap values at indexes i & j
    def swap(self, i, j):
        v = self()
        v[i] = self[j]
        v[j] = self[i]
        return v
