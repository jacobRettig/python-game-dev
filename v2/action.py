'''
Created on May 13, 2015

@author: jacobrettig
'''

class Action():
    def __init__(self, onStart=None):
        self.owner = None
        self._onStart = onStart
        self.action = None
        
    def setOnStart(self, onStart):
        self._onStart = onStart
        return self
    def onStart(self, *args, **kwargs):
        if self._onStart is not None:
            return self.onStart(self, *args, **kwargs)
    
    def __call__(self, owner):
        self.owner = owner
        return self
    
#     True if keep cycling
    def onCycle(self, *args, **kwargs):
        if self._onCycle is not None:
            return self._onCycle(self, *args, **kwargs)
        return False
    def setOnCycle(self, onCycle):
        self._onCycle = onCycle
        return self

@Action
def slash(self):
    self.action = 'slash'
