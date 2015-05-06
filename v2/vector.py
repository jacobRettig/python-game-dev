'''
Created on Apr 20, 2015

@author: jacobrettig
'''
from collections import Iterable
import math, functools


class Vector(Iterable):
    def __init__(self, *args):
        self.size = len(args)
        self.dat = [0] * len(self)
        self.dat[:] = args[:]
        
    TAU = math.pi * 2
    
    def __str__(self):
        return "[" + self.reduce((lambda x, y: str(x) + ", " + str(y))) + "]"
    
    def __len__(self):
        return self.size
    
    def __call__(self):
        return Vector(*self)
    
    def map(self, fn, *args):
        self[:] = list(map(fn, self, *self.prep(*args)))
        return self
        
    def reduce(self, fn, *args):
        return functools.reduce(fn, self, *args)
        
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
    
    def __add__(self, o):
        v = self()
        return v.map((lambda x, y: x + y), o)
    def __radd__(self, o):
        v = self()
        return v.map((lambda x, y: y + x), o)
    def __iadd__(self, o):
        return self.map((lambda x, y: x + y), o)
    
    def __sub__(self, o):
        v = self()
        return v.map((lambda x, y: x - y), o)
    def __rsub__(self, o):
        v = self()
        return v.map((lambda x, y: y - x), o)
    def __isub__(self, o):
        return self.map((lambda x, y: x - y), o)
        
    def __mul__(self, o):
        v = self()
        return v.map((lambda x, y: x * y), o)
        
    def __rmul__(self, o):
        v = self()
        return v.map((lambda x, y: y * x), o)
        
    def __imul__(self, o):
        return self.map((lambda x, y: x * y), o)
        
    def __truediv__(self, o):
        v = self()
        return v.map((lambda x, y: x / y), o)
        
    def __rtruediv__(self, o):
        v = self()
        return v.map((lambda x, y: y / x), o)
        
    def __itruediv__(self, o):
        return self.map((lambda x, y: x / y), o)
    
    def __floordiv__(self, o):
        v = self()
        return v.map((lambda x, y: x // y), o)
        
    def __rfloordiv__(self, o):
        v = self()
        return v.map((lambda x, y: y // x), o)
        
    def __ifloordiv__(self, o):
        return self.map((lambda x, y: x // y), o)
    
    def __mod__(self, o):
        v = self()
        return v.map((lambda x, y: x % y), o)
        
    def __rmod__(self, o):
        v = self()
        return v.map((lambda x , y: y % x), o)
        
    def __imod__(self, o):
        return self.map((lambda x, y: x % y), o)
        
    def __pow__(self, o):
        v = self()
        return v.map((lambda x, y: x ** y), o)
        
    def __rpow__(self, o):
        v = self()
        return v.map((lambda x, y: y ** x), o)
        
    def __ipow__(self, o):
        return self.map((lambda x, y: x ** y), o)
        
    def __neg__(self):
        v = self()
        return v.map((lambda x: -x))
        
    def __abs__(self):
        v = self()
        return v.map((lambda x: abs(x)))
        
    def __pos__(self):
        v = self()
        return v.map((lambda x: +x))
        
    def swap(self, i, j):
        v = self()
        v[i] = self[j]
        v[j] = self[i]
        return v
        
