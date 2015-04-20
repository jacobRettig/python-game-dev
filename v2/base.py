'''
Created on Apr 20, 2015

@author: jacobrettig
'''

class Base():
    def __getattr__(self, k):
        if isinstance(k, str) and k.find("_get_") != 0 and hasattr(self, "_get_" + k): 
            return getattr(self, "_get_" + k)()
        raise AttributeError
    
    def __setattr__(self, k, v):
        if isinstance(k, str) and not hasattr(self, k) and hasattr(self, "_set_" + k):
            return getattr(self, "_set_" + k)(v)
        self.__dict__[k] = v
        return self.__dict__[k]
    
    
