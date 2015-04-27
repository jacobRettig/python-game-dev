'''
Created on Apr 27, 2015

@author: jacobrettig
'''

import math
from random import Random

from base import Base


rand = Random()


class Map(Base):
    TileCode = {"EMPTY":0,
        "WALL":1,
        "NODE":2,
        "PLAYER":3}
    TileText = {" ":"EMPTY",
        "#":"WALL",
        "N":"NODE",
        "P":"PLAYER"}
    
    def __init__(self, base, cellWidth, cellHeight, textWidth,textHeight):
        self._base_, self._baseW_, self._baseH_ = base, textWidth, textHeight
        self.cellWidth, self.cellHeight = cellWidth, cellHeight
        
    def _get_base(self):
        return self._base_
    def set_base(self, v):
        raise AttributeError
    def _get_baseW(self):
        return self._baseW_
    def set_baseW(self, v):
        raise AttributeError
    def _get_baseH(self):
        return self._baseH_
    def set_baseH(self, v):
        raise AttributeError
    
    def reset(self, player):
        self.entityList = []
        self.openCells = []
        self.player = player
        
        self.data = [[Map.TileCode["EMPTY"]] * self.baseW] * self.baseH
        self.metaData = [{} * self.baseW] * self.baseH
        self.nodes = []
        
        for i in range(self.baseW * self.baseH):
            x, y = i // self.baseW, i % self.baseW
            
            self.data[x][y] = Map.TileCode[Map.TileText[i]]
            
            if Map.TileText[i] != "WALL" and Map.TileText[i] != "PLAYER":
                self.openCells.append((x, y))
            if Map.TileText[i] == "NODE":
                self.initNode(x, y)
    
        
    def initNode(self, x, y):
        self.metaData[x][y]["NODE"] = []
        for node in self.nodes:
            if (node[0] == x or node[1] == y) and self.isOpenLinePerpendicular(x, y, node[0], node[y]):
                self.metaData[node[0]][node[1]]["NODE"].append((x, y))
                self.metaData[x][y]["NODE"].append((node[0], node[1]))
                
        self.nodes.append((x, y))
        
    def isOpenLinePerpendicular(self, x1, y1, x2, y2):
        if x2 - x1 == 0:
            if y2 - y1 < 0:
                for y in range(y1 - y2 - 1):
                    if self.data[x1][y2 + y + 1] == self.TileCode["WALL"]:
                        return False
            else:
                for y in range(y2 - y1 - 1):
                    if self.data[x1][y1 + y + 1] == self.TileCode["WALL"]:
                        return False
        elif y2 - y1 == 0:
            if x2 - x1 < 0:
                for x in range(x1 - x2 - 1):
                    if self.data[x2 + x + 1][y1] == self.TileCode["WALL"]:
                        return False
            else:
                for x in range(x2 - x1 - 1):
                    if self.data[x1 + x + 1][y1] == self.TileCode["WALL"]:
                        return False    
        else:
            raise TypeError("Not perpendicular line")
        return True
        
    def spawnEntity(self, entity):
        w, h = self.cellWidth - entity.width, self.cellHeight - entity.height
        pos, x, y = self.openCells[rand.randrange(0, len(self.openCells))], rand.random() * w, rand.random() * h
        entity.x, entity.y = pos[0]*self.cellWidth + x, pos[1]*self.cellHeight + y
        self.entityList.append(entity)
        
        
    
        
    