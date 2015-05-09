'''
Created on May 9, 2015

@author: lisarettig
'''

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
            raise AttributeError, "can't set attribute"
        return self._set(inst, value)

    def __delete__(self, inst):
        if self._del is None:
            raise AttributeError, "can't delete attribute"
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
        return delattr(recut(getattr, (inst,) + self.path), self.attr)