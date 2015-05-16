'''
Created on May 13, 2015

@author: jacobrettig
'''

from entity import Mob

class Action():
    def __init__(self, action, onStart=None):
        if action is not None and not isinstance(action, str):
            raise TypeError('action = {a}    type = {t}'.format(a=action, t=type(action)))
        self._onStart = onStart
        self._onCycle = None
        self.action = action
        
    def setOnStart(self, onStart):
        self._onStart = onStart
        return self
    def onStart(self, owner):
        if self._onStart is not None:
            return self._onStart(self, owner)
    
    def __call__(self, onStart):
        return Action(self.action, onStart)
    
    def setOnCycle(self, onCycle):
        self._onCycle = onCycle
        return self
    def onCycle(self, owner):
        if self._onCycle is not None:
            return self._onCycle(self, owner)
        else:
            owner.action = -1

@Action('slash')
def slash(self, owner):
    for seen in owner.seen:
        if isinstance(seen, Mob) and seen.hypot(owner.cen) <= 15:
            seen.hp -= 2
            
@Action('stab')
def stab(self, owner):
    for seen in owner.seen:
        if isinstance(seen, Mob) and seen.hypot(owner.cen) <= 10:
            seen.hp -= 3
             
    
    
    