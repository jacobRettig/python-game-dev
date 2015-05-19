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
        self.set_colorkey(self.get_at((0, 0)))
    def __getitem__(self, k):
        return self.subsurface((k[1] * self.get_width() / 13,
                                k[0] * self.get_height() / 21, 
                                self.get_width() / 13, 
                                self.get_height() / 21))
    

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
        'gender':{
                  'DEFAULT':'male',
                  'male':{}, 
                  'female':{}
                  },
        'body':{
                'DEFAULT':'light',
                'light':{}, 
                'dark':{}, 
                'dark2':{}, 
                'darkelf':{}, 
                'darkelf2':{}, 
                'tanned':{}, 
                'tanned2':{}, 
                'skeleton':{
                            'gender':{
                                      'include':set(('male',))
                                      },
                            'eyes':{
                                    'include':set(('none',))
                                    },
                            'nose':{
                                    'include':set(('none',))
                                    },
                            'ears':{
                                    'include':set(('none',))
                                    },
                            'hair':{
                                    'include':set(('none',))
                                    },
                            'beard':{
                                    'include':set(('none',))
                                    }
                            }
                },
        'eyes':{
                'DEFAULT':'blue',
                'blue':{}, 
                'brown':{}, 
                'gray':{}, 
                'green':{}, 
                'orange':{}, 
                'purple':{}, 
                'red':{}, 
                'yellow':{}, 
                'none':{}
                },
        'nose':{
                'DEFAULT':'big',
                'big':{}, 
                'button':{}, 
                'straight':{}, 
                'none':{}
                },
        'ears':{
                'DEFAULT':'big',
                'big':{}, 
                'elven':{}, 
                'none':{}
                },
        'hair color':{'DEFAULT':'black', 'black':{}, 'blonde':{}, 'blonde2':{}, 'blue':{}, 'blue2':{}, 'brunette':{}, 'brunette2':{}, 'dark-blonde':{}, 'gold':{},
            'gray':{}, 'gray2':{}, 'light-blonde':{}, 'light-blonde2':{}, 'pink':{}, 'pink2':{}, 'purple':{}, 'raven':{}, 'raven2':{}, 'redhead':{},
            'redhead2':{}, 'ruby-red':{}, 'white-blonde':{}, 'white-blonde2':{}, 'white-cyan':{}, 'white':{}},
        'hair':{'DEFAULT':'plain', 'none':{}, 'bangs':{}, 'bangslong':{}, 'bangslong2':{}, 'bangsshort':{}, 'bedhead':{}, 'bunches':{}, 'jewfro':{}, 'long':{},
            'long':{}, 'longhawk':{}, 'longknot':{}, 'loose':{}, 'messy1':{}, 'messy2':{}, 'mohawk':{}, 'page':{}, 'page2':{}, 'parted':{}, 'pixie':{},
            'plain':{}, 'poneytail':{}, 'poneytail2':{}, 'princess':{}, 'shorthawk':{}, 'shortknot':{}, 'shoulderl':{}, 'shoulderr':{}, 'swoop':{},
            'unkempt':{}, 'xlong':{}, 'xlongknot':{}},
        'beard':{'DEFAULT':'none', 'none':{}, 'bigstache':{}, 'fiveoclock':{}, 'frenchstache':{}, 'mustache':{}},
        'shirt':{'DEFAULT':'brown', 'none':{}, 'brown':{}, 'maroon':{}, 'teal':{}, 'white':{}},
        'pants':{'DEFAULT':'teal', 'none':{}, 'magenta':{}, 'red':{}, 'teal':{}, 'white':{}, 'skirt':{}},
        'shoes':{'DEFAULT':'black', 'none':{}, 'black':{}, 'brown':{}, 'maroon':{}},
        'left hand':{'DEFAULT':'none', 'none':{}, 'arrow':{}, 'arrow_skeleton':{}},
        'right hand':{'DEFAULT':'none', 'none':{}, 'bow':{}, 'bow_skeleton':{}, 'greatbow':{}, 'recurvebow':{},
                      'dagger':{
                                'gender':{
                                          'include':'male'
                                          }
                                },
                      'spear':{
                               'gender':{
                                         'include':'male'
                                         }
                               },
                      'woodwand':{
                                  'gender':{
                                            'include':'male'
                                            }
                                  }
                      }
        }
    
    @staticmethod
    def fixLpcTag(tag, layer=0):
        if layer == 2:
            class includeAll(frozenset):
                def __init__(self):
                    pass
                def __contains__(self, *args, **kwargs):
                    return True
            class excludeAll(frozenset):
                def __init__(self):
                    pass
                def __contains__(self, *args, **kwargs):
                    return False
            
            for k in tag:
                if isinstance(tag[k], dict):
                    tag[k].setdefault('include', includeAll())
                    tag[k].setdefault('exclude', excludeAll())
        else:
            for k in tag:
                tag[k] = LPC.fixLpcTag(tag[k], layer + 1)
        return tag
#     TAG = fixLpcTag(TAG)
    
    def __init__(self, world, **kwargs):
        self.world = world
        self.data, self._image = {}, None
        for key in self.TAG:
            self.data[key] = self.TAG[key]['DEFAULT']
            
        for key in kwargs:
            self[key] = kwargs[key]
    
    def __getitem__(self, k):
        if k in self.data:
            return self.data[k]
        else:
            raise IndexError('Nonexistent index : {k}'.format(k=k))
    def __setitem__(self, k, v):
        if not v in self.TAG[k]:
            raise IndexError('SpriteSheetLPC assignment error value : {value} is not in key : {key}  available options are {options}'
                             .format(value=v, key = k, options=self.TAG[k]))
        
        self.data[k] = v
        for includer in self.data:
            for feature in (dat for dat in self.data if dat != includer and dat in self.TAG[includer][self[includer]]):
                
                self.TAG[includer][self[includer]][feature].setdefault('include', [self[feature]])
                self.TAG[includer][self[includer]][feature].setdefault('exclude', [])
                
                if self[feature] not in self.TAG[includer][self[includer]][feature]['include']:
                    raise LpcTagAssignmentError('tried to assign feature : {k}  value : {v}  but {featureVal} of {feature} not in inclusion for {includer}'
                                                .format(k=k, v=v, featureVal=self[feature], feature=feature, includer=includer))
                if self[feature] in self.TAG[includer][self[includer]][feature]['exclude']:
                    raise LpcTagAssignmentError('tried to assign feature : {k}  value : {v}  but {featureVal} of {feature} is in exclusion for {includer}'
                                                .format(k=k, v=v, featureVal=self[feature], feature=feature, includer=includer))
    
        self._image = None
        
    def __call__(self):
        lpc = LPC(self.world)
        for k in self.data:
            lpc[k] = self.data[k]
        return lpc
        
    def __iter__(self):
        return dict(self.data, **{tag:0 for tag in self.TAG.keys() if tag not in self.data})
    
    layer1 = frozenset(('eyes', 'nose', 'ears'))
    layer2 = frozenset(('shirt', 'pants', 'shoes'))
    layer3 = frozenset(('beard', 'hair'))
    layer4 = frozenset(('left hand', 'right hand'))
    @property    
    def image(self):
        if self._image is None:
            image = self.getSheet('body', self.data)
            TAG = self.TAG
            for idn in ('eyes', 'nose', 'ears'):
                if self[idn] != 'none':
                    image.blit(self.getSheet(idn, self.data), (0, 0))
            
            for part in (self.layer1, self.layer2, self.layer3, self.layer4):
                for idn in part:
                    if self[idn] != 'none':
                        image.blit(self.getSheet(idn, self.data), (0, 0))
                        
            self._image = image
        return self._image
    
    def getSheet(self, idn, tag):
        path = self.getSheetPath(idn, tag)
        if not (path in self.world.loadedSheets):
            self.world.loadedSheets[path] = ImageLPC(path + '.png')
        return self.world.loadedSheets[path]
    
    def getSheetPath(self, idn, tag):
        TAG = LPC.TAG

        if self[idn] == 'none':
            raise TypeError('tag : {tag}  is none'.format(tag=idn))
        
        path = 'Universal-LPC-spritesheetTmp/'
        gender = self['gender']
        if idn in ('gender', 'hair color') or not (idn in TAG.keys()):
            raise AttributeError
        elif idn in ('body', 'eyes', 'nose', 'ears'):
            path += 'body/' + gender + "/"
            
            if idn != 'body':
                path += idn + '/'
            path += self[idn]
            if idn in ('nose' 'ears'):
                path += idn + "_" + self['body']
        elif idn in ('hair', 'beard'):
            if idn == 'hair':
                path += 'hair/'
            else:
                path += 'facial/'
            path += gender + '/' + self[idn] + '/'
            path += self['hair color']
        elif idn == 'pants':
            path += 'legs/'
            if self['pants'] == 'skirt':
                path += 'skirt/' + gender + '/robe_skirt_' + gender
                if gender == 'female':
                    path += '_incomplete'
            else:
                path += 'pants/' + gender + '/' + self['pants'] + '_pants_' + gender 
        elif idn == 'shirt':
            path += 'torso/shirts/'
            if gender == 'male':
                path += 'longsleeve/male/' + self['shirt'] + '_longsleeve'
            else:
                path += 'sleeveless/female/' + self['shirt'] + '_sleeveless'
        elif idn == 'shoes':
            path += 'feet/shoes/' + gender + "/" + self['shoes'] + '_shoes_' + gender
        elif idn in ('left hand', 'right hand'):
            if idn == 'right hand' and self['right hand'] in ('dagger', 'spear', 'woodwand'):
                path += 'weapons/right hand/male/' + self['right hand'] + "_male" 
            else:
                path += 'weapons/' + idn + '/either/' + self[idn]
                
        return path

class AnimationLPC():
    ACTIONS = {'cast':3, 'thrust':0, 'walk':2, 'slash':1, 'shoot':4, 'none':2}
    
    def __init__(self, owner, spriteSheet=None, **kwargs):
        self.owner, self.spriteSheet = owner, spriteSheet
        if self.spriteSheet is None:
            self.spriteSheet = LPC(self.owner.world)
        
        self.action = 'none'
        self.speed = 8
        self.dirx, self.diry = 1, 0
        self.cycles = 0
        self.time = self.owner.time
        
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
    
    def __getitem__(self, k):
        return self.spriteSheet[k]
    def __setitem__(self, k, v):
        self.spriteSheet[k] = v
    
    @property
    def image(self):
        self.dirx, self.diry = self.owner.dir.x, self.owner.dir.y
        if self.owner.action != self.action:
            self.action = self.owner.action
            self.time, self.cycles = self.owner.time, 0
        time = self.owner.time - self.time
        
        self.cycles = int(time // self.speed)
        index = int((time % self.speed) * self.frames // self.speed)
        
        dirc = 0
        if abs(self.dirx) > abs(self.diry):
            if self.dirx > 0:
                dirc = 3
            else:
                dirc = 1
        elif self.diry > 0:
            dirc = 2
            
        if self.action == 'hurt':
            return self.spriteSheet.image[20, index]
        
        return self.spriteSheet.image[self.ACTIONS[self.action]*4 + dirc, index]
    
    @image.setter
    def image(self, v):
        raise AttributeError
    
    @property
    def frames(self):
        if self.action is 'none':
            return 1
        elif self.action is 'cast':
            return 7
        elif self.action is 'thrust':
            return 8
        elif self.action is 'walk':
            return 9
        elif self.action is 'slash':
            return 6
        elif self.action is 'shoot':
            return 13
        elif self.action is 'hurt':
            return 6
        else:
            raise AttributeError('action not found action: {}'.format(self.action))

class LpcTagAssignmentError(Exception):
    pass