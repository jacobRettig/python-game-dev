'''
Created on May 5, 2015

@author: jacobrettig
'''

import pygame

class ImageLPC(pygame.Surface):
    def __init__(self, path):
        img = pygame.image.load(path)
        pygame.Surface.__init__(self, (img.get_width(), img.get_height()))
        self.blit(img, (0, 0))
        
    def __getitem__(self, k):
        return self.subsurface((k[1] * self.get_width() / 13, k[0] * self.get_height() / 21, self.get_width() / 13, self.get_height() / 21))
    

class SpriteSheetMaster():
    def __init__(self, size=-1):
        self.size, self.images, self.paths = size, {}, []
        
    def __len__(self):
        return len(self.paths)
    
    def __getitem__(self, k):
        if isinstance(k, str):
            if k in self.paths:
                self.paths.append(self.paths.pop(self.paths.index(k)))
            else:
                if len(self) == self.size:
                    del(self.images[self.paths.pop(0)])
                self.images[k] = ImageLPC(k)
                self.paths.append(k)
            return self.images[k]
        raise AttributeError
                
class LPC():
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
    
    def __init__(self, master, **kwargs):
        self.master, self.data, self._image_ = master, {}, None
        for key in kwargs.keys():
            self[key] = kwargs[key]
    
    def __getitem__(self, k):
        if k in self.data.keys():
            return self.TAG[k][self.data[k]]
        else:
            return self.TAG[k][0]
    def __setitem__(self, k, v):
        if v is 0:
            del(self.data[k])
        else:
            self.data[k] = self.TAG[k].index(v)
        self._image_ = None
        
    def __iter__(self):
        return dict(self.data, **{tag:0 for tag in self.TAG.keys() if tag not in self.data})
    
    @property    
    def image(self):
        if self._image_ is None:
            image = self.getSheet('body', self.tag)
            TAG = self.TAG
            for idn in ('eyes', 'nose', 'ears'):
                image.blit(self.getSheet(idn, self.tag), (0, 0))
            
            for part in (('eyes', 'nose', 'ears'), ('shirt', 'pants', 'shoes'), ('beard', 'hair'),
                 ('left hand', 'right hand')):
                for idn in part:
                    if TAG[idn][self[idn]] != 'none':
                        image.blit(self.getSheet(idn, self.tag), (0, 0))
                        
            self._image_ = image
        return self._image_
    
    def getSheet(self, idn, tag):
        path = self.getSheetPath(idn, tag)
        if not (path in self.sheets):
            self.sheets[path] = pygame.image.load(path + '.png')
        return self.sheets[path]
    
    def getSheetPath(self, idn, tag):
        TAG = LPC.TAG

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

class AnimationLPC():
    ACTIONS = {'cast':3, 'thrust':0, 'walk':2, 'slash':1, 'shoot':4}
    
    def __init__(self, owner, spriteSheet=None, **kwargs):
        self.owner, self.spriteSheet = owner, spriteSheet
        if self.spriteSheet is None:
            self.spriteSheet = LPC(owner, SpriteSheetMaster())
        
        self.action = 'none'
        self.speed = 5
        self.dx, self.dy = 1, 0
        self.cycles = 0
        self.time = self.owner.time
        
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
            
        @property
        def image(self):
            if not self.owner.dx == 0 or not self.owner.dy == 0:
                self.dx, self.dy = self.owner.dx, self.owner.dy
            if self.owner.action != self.action:
                self.action = self.owner.action
                self.time, self.cycles = self.owner.time, 0
            time = self.owner.time - self.time
            
            self.cycles = int(time // self.speed)
            index = int((time % self.speed) * self.frames // self.speed)
            
            dirc = 0
            if abs(self.dx) > abs(self.dy):
                if self.dx > 0:
                    dirc = 3
                else:
                    dirc = 1
            elif self.dy > 0:
                dirc = 2
                
            if self.action == 'hurt':
                return self.spriteSheet[(20, index)]
            
            return self.spriteSheet[(self.ACTIONS[self.action]*4 + dirc, index)]
        
        @image.setter
        def image(self, v):
            raise AttributeError
