'''
Created on May 4, 2015

@author: jacobrettig
'''

from animation import Animation
Ani = Animation

class Animation(Ani):
    def __init__(self, owner, iterationSpeed):
        Ani.__init__(self, owner, None, iterationSpeed)
        
    @property
    def images(self):
        pass