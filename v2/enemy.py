'''
Created on Apr 29, 2015

@author: jacobrettig
'''

import math

import entity

class Enemy(entity.EntityVision):
    def __init__(self, world, pos, prevNode, nextNode, direction=(1,0), speed=5, turnRate=math.pi/16, visDis=6, visVec=(1,0), hp=20):
        entity.EntityVision.__init__(world, pos, direction, speed, turnRate, visDis, visVec)
        self.prevNode, self.nextNode = prevNode, nextNode
        self.target = nextNode
        self.sees = []
        
    
    def update(self):
        self.sees = entity.EntityVision.sight()
        return entity.EntityVision.update(self)
    
        
        
    