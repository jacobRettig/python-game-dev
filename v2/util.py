'''
Created on May 9, 2015

@author: lisarettig
'''

from collections import Iterable
from functools import reduce

from vector2d import Vector2D


class InstanceGuard(object):
    def __init__(self, name, defaultFn, fset=None, fget=None, fdel=None, doc=None, **kwargs):
        self.name = name
        self.defaultFn = defaultFn
        self._get = fget
        self._set = fset
        self._del = fdel
        
        for key, value in kwargs.items():
            setattr(self, "_{}".format(key), value)
            

    def __call__(self, fn, *args, **kwargs):
        kwargs[self.defaultFn] = fn
        return InstanceGuard(self.name, self.defaultFn, *args, **kwargs)

    def getter(self, fn):
        self.__get = fn
        return self
    
    def setter(self, fn):
        self.__set = fn
        return self
    
    def deleter(self, fn):
        self.__del = fn
        return self

    def __get__(self, inst, type=None):
        if inst is None:
            return self
        if self._get is None:
            return getattr(inst, self.name)
        return self._get(inst)

    def __set__(self, inst, value):
        if self._set is None:
            raise AttributeError("can't set attribute")
        return self._set(inst, value)

    def __delete__(self, inst):
        if self._del is None:
            raise AttributeError("can't delete attribute")
        return self._del(inst)
    
    
class GS(object):
    def __init__(self, attr, *path):
        self.path, self.attr = path, attr
        
    def __get__(self, inst, type=None):
        if inst is None:
            return self
        return getattr(reduce(getattr, (inst,) + self.path), self.attr)

    def __set__(self, inst, value):
        setattr(reduce(getattr, (inst,) + self.path), self.attr, value)

    def __delete__(self, inst):
        return delattr(reduce(getattr, (inst,) + self.path), self.attr)
    
    
class Vector2DReadOnly(Vector2D):
    def __init__(self, *args):
        self.hasInit = False
        Vector2D.__init__(self, *args)
        self.hasInit = True
    
    def __setitem__(self, key, value):
        raise AttributeError
    

class Vector2DCustom(Vector2D, Iterable):
    def __init__(self, fGet=None, fSet=None, **kwargs):
        self.fGet = fGet
        self.fSet = fSet
        if 'get' in kwargs.keys():
            self.fGet = kwargs['get']
        if 'set' in kwargs.keys():
            self.fSet = kwargs['set']
            
    def getter(self, fn):
        self.fGet = fn
        return self
    
    def setter(self, fn):
        self.fSet = fn
        return self
    
    def __len__(self):
        return 2
    
    def __call__(self):
        return Vector2D(self.x, self.y)
    
    @property
    def list(self):
        return [self.x, self.y]
    
    def __iter__(self):
        return self.list.__iter__()
    def __next__(self):
        return self.list.__next__()
    def next(self):
        return self.list.next()
    
    def __getitem__(self, key):
        if self.fGet is None:
            raise AttributeError("Getter not defined")
        else:
            return self.fGet(self, key)
    
    def __setitem__(self, key, value):
        if self.fSet is None:
            raise AttributeError("Setter not defined")
        else:
            return self.fSet(key)
        
    
