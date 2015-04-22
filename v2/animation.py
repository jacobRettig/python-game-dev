'''
Created on Apr 22, 2015

@author: jacobrettig
'''

import math

import pygame

from base import Base

def loadImages(path, extension, amount, isCardinal=True, resize=False, width=50, height=50):
    if isCardinal:
        imgs = [None] * 8
        cardinal = ("n", "ne", "nw", "s", "se", "sw", "e", "w")
        for i in range(8):
            imgs[i] = [None]*imgs
            for j in range(amount):
                imgs[i][j] = pygame.image.load(path + cardinal[i] + str(j) + "0000"[len(str(j)):] + "." + extension)
                imgs[i][j].set_colorkey(imgs[i][j].get_at((0, 0)))
                if resize:
                    imgs[i][j] = pygame.transform.scale(imgs[i][j], (width, height))
        return imgs
    else:
        imgs = [None] * amount
        for j in range(amount):
            imgs[i] = pygame.image.load(path + str(i) + "0000"[len(str(i)):] + "." + extension)
            imgs[i].set_colorkey(imgs[i].get_at((0, 0)))
            if resize:
                imgs[i] = pygame.transform.scale(imgs[i], (width, height))
        return imgs

class Animation(Base):
    N = 0
    NE = 1
    NW = 2
    S = 3
    SE = 4
    SW = 5
    E = 6
    W = 7
    
    def __init__(self, owner, images, iterationSpeed):
        self.owner, self.images, self.iterationSpeed = owner, images, iterationSpeed
        self.imageAmount = len(self.images[0])
        self.timeInit = 0
        
    def start(self):
        self.timeInit = self.owner.world.time
    
    cos, sin = math.cos, math.sin
    PI = math.pi
    
    c1, s1 = cos(PI/8), sin(PI/8)
    c2, s2 = cos(3*PI/8), sin(3*PI/8)
    c3, s3 = cos(5*PI/8), sin(5*PI/8)
    c4, s4 = cos(7*PI/8), sin(7*PI/8)
    c5, s5 = cos(9*PI/8), sin(9*PI/8)
    c6, s6 = cos(11*PI/8), sin(11*PI/8)
    c7, s7 = cos(13*PI/8), sin(13*PI/8)
    c8, s8 = cos(15*PI/8), sin(15*PI/8)
    def _get_image(self):
        dx, dy = self.owner.dx, self.owner.dy
        step = ((self.owner.world.time - self.timeInit) // self.iterationSpeed) % self.imageAmount
        if dy > 0:
            if dy*Animation.c4 - dx*Animation.s4 > 0:
                return self.images[Animation.W][step]
            elif dy*Animation.c3 - dx*Animation.s3 > 0:
                return self.images[Animation.NW][step]
            elif dy*Animation.c2 - dx*Animation.s2 > 0:
                return self.images[Animation.N][step]
            elif dy*Animation.c1 - dx*Animation.s1 > 0:
                return self.images[Animation.NE][step]
            else:
                return self.images[Animation.E][step]
        else:
            if dy*Animation.c5 - dx*Animation.s5 > 0:
                return self.images[Animation.W][step]
            elif dy*Animation.c6 - dx*Animation.s6 > 0:
                return self.images[Animation.SW][step]
            elif dy*Animation.c7 - dx*Animation.s7 > 0:
                return self.images[Animation.S][step]
            elif dy*Animation.c8 - dx*Animation.s8 > 0:
                return self.images[Animation.SE][step]
            else:
                return self.images[Animation.E][step]

    def _set_image(self, k):
        raise AttributeError

