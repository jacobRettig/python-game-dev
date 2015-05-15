'''
Created on May 4, 2015

@author: jacobrettig
'''
from collections import Iterable

import pygame


class SpriteSheetControl():
    TAG = {
        'gender':('male', 'female'),
        'body':('light', 'dark', 'dark2', 'darkelf', 'darkelf2', 'tanned', 'tanned2'),
        'eyes':('blue', 'brown', 'gray', 'green', 'orange', 'purple', 'red', 'yellow'),
        'nose':('big', 'button', 'straight'),
        'ears':('big', 'elven'),
        'hair color':('black', 'blonde', 'blonde2', 'blue', 'blue2', 'brunette', 'brunette2', 'dark-blonde', 'gold',
            'gray', 'gray2', 'light-blonde', 'light-blonde2', 'pink', 'pink2', 'purple', 'raven', 'raven2', 'redhead',
            'redhead2', 'ruby-red', 'white-blonde', 'white-blonde2', 'white-cyan', 'white'),
        'hair':('none', 'bangs', 'bangslong', 'bangslong2', 'bangsshort', 'bedhead', 'bunches', 'jewfro', 'long',
            'long', 'longhawk', 'longknot', 'loose', 'messy1', 'messy2', 'mohawk', 'page', 'page2', 'parted', 'pixie',
            'plain', 'poneytail', 'poneytail2', 'princess', 'shorthawk', 'shortknot', 'shoulderl', 'shoulderr', 'swoop',
            'unkempt', 'xlong', 'xlongknot'),
        'beard':('none', 'bigstache', 'fiveoclock', 'frenchstache', 'mustache'),
        'shirt':('none', 'brown', 'maroon', 'teal', 'white'),
        'pants':('none', 'magenta', 'red', 'teal', 'white', 'skirt'),
        'shoes':('none', 'black', 'brown', 'maroon'),
        'left hand':('none', 'arrow', 'arrow_skeleton'),
        'right hand':('none', 'bow', 'bow_skeleton', 'greatbow', 'recurvebow')
        }
    
    def __init__(self):
        self.resetLoaded()
        
    @staticmethod
    def isValidnParam(key, value):
        return key in SpriteSheetControl.TAG and value in SpriteSheetControl.TAG[key]
    
    def resetLoaded(self):
        self.sheets = {}
        
    def getSheet(self, idn, tag):
        path = self.getSheetPath(idn, tag)
        if not (path in self.sheets):
            self.sheets[path] = pygame.image.load(path + '.png')
        return self.sheets[path]
    
    def getSheetPath(self, idn, tag):
        TAG = SpriteSheetControl.TAG

        if TAG[idn][tag[idn]] == 'none':
            return self.EMPTY
        
        path = 'Universal-LPC-spritesheetTmp/'
        gender = TAG['gender'][tag['gender']]
        if idn in ('gender', 'hair color') or not (idn in TAG.keys()):
            raise AttributeError
        elif idn in ('body', 'eyes', 'nose', 'ears'):
            path += 'body/' + gender + "/"
            
            if idn != 'body':
                path += idn + '/'
            path += TAG[idn][tag[idn]]
            if idn in ('nose' 'ears'):
                path += idn + "_" + TAG['body'][tag['body']]
        elif idn in ('hair', 'beard'):
            if idn == 'hair':
                path += 'hair/'
            else:
                path += 'facial/'
            path += gender + '/' + TAG[idn][tag[idn]] + '/'
            path += TAG['hair color'][tag['hair color']]
        elif idn == 'pants':
            path += 'legs/'
            if TAG['pants'][tag['pants']] == 'skirt':
                path += 'skirt/' + gender + '/robe_skirt_' + gender
                if gender == 'female':
                    path += '_incomplete'
            else:
                path += 'pants/' + gender + '/' + TAG['pants'][tag['pants']] + '_pants_' + gender 
        elif idn == 'shirt':
            path += 'torso/shirts/'
            if gender == 'male':
                path += 'longsleeve/male/' + TAG['shirt'][tag['shirt']] + '_longsleeve'
            else:
                path += 'sleeveless/female/' + TAG['shirt'][tag['shirt']] + '_sleeveless'
        elif idn == 'shoes':
            path += 'feet/shoes/' + gender + "/" + TAG['shoes'][tag['shoes']] + '_shoes_' + gender
        elif idn in ('left hand', 'right hand'):
            path += 'weapons/' + idn + '/either/' + TAG[idn][tag[idn]]
                
        return path
            
        @property
        def EMPTY(self):
#             TODO fix size (i.e. random number right now)
            return pygame.Surface((123, 456))
            
            
            
            

class SpriteSheet():
#     by default all values are 0 indexed
    def __init__(self, masterSpriteSheet=None, **params):
        self.MSS = masterSpriteSheet
        if self.MSS is None:
            self.MSS = SpriteSheetControl()
        
        self._tag_ = {}
        self._image_ = None
        
        for idn in SpriteSheetControl.TAG.keys():
            self.tag[idn] = 0
            
        for idn in params.keys():
            idn2 = idn.replace("_", " ", 999)
            if not (idn2 in SpriteSheetControl.TAG):
                raise TagError(idn, params[idn], True)
            elif not (params[idn] in SpriteSheetControl.TAG[idn2]):
                raise TagError(idn, params[idn], False)
            else:
                self.tag[idn2] = SpriteSheetControl.TAG[idn2].index(params[idn])
                
    @property
    def image(self):
        if self._image_ is None:
            image = self.MSS.getSheet('body', self.tag)
            TAG = SpriteSheetControl.TAG
            for idn in ('eyes', 'nose', 'ears'):
                image.blit(self.MSS.getSheet(idn, self.tag), (0, 0))
            
            for part in (('eyes', 'nose', 'ears'), ('shirt', 'pants', 'shoes'), ('beard', 'hair'),
                 ('left hand', 'right hand')):
                for idn in part:
                    if TAG[idn][self.tag[idn]] != 'none':
                        image.blit(self.MSS.getSheet(idn, self.tag), (0, 0))
                        
            self._image_ = image
        return self._image_
    @image.setter
    def image(self, value):
        raise AttributeError

    @property
    def tag(self):
        return self._tag_
#     improve so setting isn't necessary
    @tag.setter
    def tag(self, value):
        self._tag_ = value
        self._image_ = None
        
class TagError(Exception):
    def __init__(self, idn, key, isID):
        self.idn, self.key, self.isID = idn, key, isID
        
    def __str__(self):
        if self.isID:
            return "Invalidn tag idn  [idn : " + repr(self.idn) + ", key : " + repr(self.key) + "]"
        else:
            return "Invalidn tag key [idn : " + repr(self.idn) + ", key : " + repr(self.key) + "]"



