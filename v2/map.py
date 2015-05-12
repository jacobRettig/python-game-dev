'''
Created on Apr 27, 2015

@author: jacobrettig
'''

import math
from random import Random

rand = Random()

class Map():
    TileCode = ["EMPTY",
        "WALL",
        "NODE",
        "PLAYER"]
    TileText = {" ":"EMPTY",
        "#":"WALL",
        "N":"NODE",
        "P":"PLAYER"}
    TileSolids = ["WALL"]
    
    def __init__(self, base, cellWidth, cellHeight, textWidth,textHeight):
        self._base_, self._baseW_, self._baseH_ = base, textWidth, textHeight
        self.cellWidth, self.cellHeight = cellWidth, cellHeight
        
    @property
    def base(self):
        return self._base_
    @base.setter
    def base(self, v):
        raise AttributeError
    @property
    def baseW(self):
        return self._baseW_
    @baseW.setter
    def baseW(self, v):
        raise AttributeError
    @property
    def baseH(self):
        return self._baseH_
    @baseH.setter
    def baseH(self, v):
        raise AttributeError
    
    def reset(self, player):
        self.entityList = []
        self.openCells = []
        self.player = player
        self.data = [[Map.TileCode.index("EMPTY")] * self.baseW] * self.baseH
        self.metaData = [{} * self.baseW] * self.baseH
        self.nodes = []
        
        for i in range(self.baseW * self.baseH):
            x, y = i // self.baseW, i % self.baseW
            
            self.data[x][y] = Map.TileCode.index(Map.TileText[i])
            
            if not (Map.TileText[i] in Map.TileSolids) and Map.TileText[i] != "PLAYER":
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
        obstacles = [Map.TileCode.index("NODE")]
        obstacles += [Map.TileCode.index(data) for data in Map.TileSolids]
        
        if x2 - x1 == 0:
            if y2 - y1 < 0:
                for tile in self.data[x1][y1:y2 + 1]:
                    if tile in obstacles: 
                        return False
            else:
                for tile in self.data[x1][y2:y1 + 1]:
                    if tile in obstacles: 
                        return False
        elif y2 - y1 == 0:
            if x2 - x1 < 0:
                for tiles in self.data[x1:x2 + 1]:
                    if tiles[y1] in obstacles:
                        return False
            else:
                for tiles in self.data[x2:x1 + 1]:
                    if tiles[y1] in obstacles:
                        return False
        else:
            raise TypeError("Not perpendicular line")
        return True
        
    def spawnEntity(self, entity):
        w, h = self.cellWidth - entity.width, self.cellHeight - entity.height
        pos, x, y = self.openCells[rand.randrange(0, len(self.openCells))], rand.random() * w, rand.random() * h
        entity.x, entity.y = pos[0]*self.cellWidth + x, pos[1]*self.cellHeight + y
        
        self.entityList.append(entity)
        
    def getSolidRange(self, x, y, w, h):
        solids = []
        if w < 0:
            x -= w
            w = -w
        if h < 0:
            y -= h
            h = -h
            
        for i in range(w):
            solids += [tile for tile in self.data[x + i][y:y+h] if Map.TileCode[tile] in Map.TileSolids]
        return solids
        
        
        
    
        
    
