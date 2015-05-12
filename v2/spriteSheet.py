'''
Created on May 2, 2015

@author: lisarettig
'''

class SpriteSheetTag():
    TAGS = {
            'gender':('male', 'female'),
            'accessories':{
                           'neck':{
                                   'type':('capeclip', 'capetie'),
                                   'color':('black', 'blue', 'brown', 'gray', 'green', 'lavender', 'maroon', 'pink', 'red', 
                                               'white', 'yellow')
                                   },
                           'necklaces':('bronze', 'gold', 'iron', 'pirate', 'silver')
                           },
            'equipment':('quiver'),
            'cape':{
                    'type':('normal', 'tattered', 'trimmed'),
                    'color':('black', 'blue', 'brown', 'gray', 'green', 'lavender', 'maroon', 'pink', 'red', 
                                               'white', 'yellow', 'whiteblue'),
                    },
            'body':{
                    'type':('dark', 'dark2', 'darkelf', 'darkelf2', 'light', 'orc', 'red orc', 'tanned', 'tanned2'),
                    'ears':{
                            'type':('big', 'eleven'),
                            'color':('dark', 'dark2', 'darkelf', 'darkelf2', 'light', 'tanned', 'tanned2'),
                            },
                    'eyes':('blue', 'brown', 'gray', 'green', 'orange', 'purple', 'red', 'yellow', 'casting eyeglow skeleton'),
                    'nose':{
                            'type':('big', 'button', 'straight'),
                            'color':('dark', 'dark2', 'darkelf', 'darkelf2', 'light', 'tanned', 'tanned2')
                            }
                    },
            'belt':{
                    'type':('buckles', 'cloth', 'leather', 'metal'),
                    'colors':('bronze', 'gold', 'iron', 'leather', 'silver', 'white', 'black', 'brown', 'teal2')
                    },
            'facial':{
                      'style':('beard', 'bigstache', 'fiveoclock', 'frenchstache', 'mustache'),
                      'color':('black', 'blonde', 'blonde2', 'blue', 'brown', 'brown2', 'brunette', 'brunette2', 'dark blonde',
                               'gold', 'gray', 'gray2', 'green', 'green2', 'light blonde', 'light blonde2', 'pink', 'pink2', 
                               'purple', 'raven', 'raven2', 'redhead', 'readhead2', 'ruby red', 'white blonde', 'white blonde2',
                               'white cyan', 'white')
                      },
            'feet':{
                    'type':('armour','shoes', 'boots', 'ghillies', 'slippers'),
                    'color':('golden', 'metal', 'brown', 'maroon', 'black', 'gray', 'white', 'ghillies')
                    },
            'formal':('bowtie', 'pants', 'shirt', 'tie', 'vest with shirt', 'vest'),
            'hair':{
                    'style':('bangs', 'bangslong', 'bangslong2', 'bangsshort', 'bedhead', 'bunches', 'jewfro', 'long', 'longhawk',
                             'longknot', 'loose', 'messy1', 'messy2', 'mohawk', 'page', 'page2', 'parted', 'pixie', 'ponytail', 
                             'ponytail2', 'princess', 'shorthawk', 'shortknot', 'shouldererl', 'shouldererr', 'swoop', 'unkempt',
                             'xlong', 'xlongknot'),
                    'color':('black', 'blonde', 'blonde2', 'blue', 'brown', 'brown2', 'brunette', 'brunette2', 'dark blonde',
                               'gold', 'gray', 'gray2', 'green', 'green2', 'light blonde', 'light blonde2', 'pink', 'pink2', 
                               'purple', 'raven', 'raven2', 'redhead', 'readhead2', 'ruby red', 'white blonde', 'white blonde2',
                               'white cyan', 'white')
                    },
            'hands':{
                     'bracelets':('bracelet'),
                     'bracers':("cloth", "leather", 'white bandages', 'white'),
                     'gloves':('golden', 'metal')
                     },
            'head':{
                    'bandanas':('red'),
                    'caps':('leather'),
                    'helms':('chainhat', 'golden', 'metal'),
                    'hoods':('chain', 'cloth'),
                    'tiaras':('bronze', 'gold', 'iron', 'purple', 'silver')
                    },
            'legs':{
                    'armour':('golden', 'metal'),
                    'pants':('magenta', 'red', 'teal', 'white'),
                    'skirt':('robe')
                    },
            'torso':{
                     'wings':('wings'),
                     'chain':('mail', 'tabard'),
                     'corset':('black', 'brown', 'red'),
                     'dress':('blue vest', 'sash', 'overskirt', 'underdress'),
                     'tightdress':('black', 'lightblue', 'red', 'white'),
                     'general':{
                                'type':('arms', 'chest', 'shoulders', 'spikes'),
                                'material':('gold', 'leather', 'plate'),
                                },
                     'robes':('black', 'blue', 'brown', 'dark brown', 'dark gray', 'forest green', 'light gray', 'purple', 'red',
                              'white'),
                     'shirts':{
                               'type':('longsleeve', 'sleeveless'),
                               'color':('brown', 'maroon', 'teal', 'white', 'teal pirate', 'white pirate')
                               },
                     'tunics':('brown', 'maroon', 'teal', 'white')
                     },
            'weapons':{
                       'both hands':('spear', 'dragonspear', 'trident'),
                       'left hand':('arrow skeleton', 'arrow', 'shield'),
                       'right hand':('bow skeleton', 'bow', 'greatbow', 'recurvebow', 'dagger', 'spear', 'steelwand', 'woodwand',
                                     'longsword', 'mace', 'rapier', 'saber')
                       }
            }
    
#     0=both, 1=female only, 2=male only
    TAG_GENDER = {
            'gender':(2, 1),
            'accessories':1,
            'equipment':0,
            'cape':1,
            'body':{
                    'type':0,
                    'ears':0,
                    'eyes':(0, 0, 0, 0, 0, 0, 0, 0, 2),
                    'nose':0
                    },
            'belt':{
                    'type':(1, 0, 0, 1),
                    'colors':(1, 1, 1, 0, 1, 0, 1, 1, 1)
                    },
            'facial':0,
            'feet':{
                    'type':(0, 0, 1, 1, 1),
                    'color':(0, 0, 0, 0, 0, 1, 1, 1)
                    },
            'formal':2,
            'hair':0,
            'hands':{
                     'bracelets':0,
                     'bracers':(1, 0, 1, 1),
                     'gloves':0
                     },
            'head':{
                    'bandanas':0,
                    'caps':0,
                    'helms':0,
                    'hoods':0,
                    'tiaras':1
                    },
            'legs':0,
            'torso':{
                     'wings':0,
                     'chain':0,
                     'corset':1,
                     'dress':1,
                     'tightdress':1,
                     'general':{
                                'type':(0, 0, 0, 2),
                                'material':0,
                                },
                     'robes':1,
                     'shirts':{
                               'type':(2, 1),
                               'color':(0, 0, 0, 0, 1, 1)
                               },
                     'tunics':1
                     },
            'weapons':{
                       'both hands':0,
                       'left hand':(0, 0, 2),
                       'right hand':(0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                       }
            }
    
    TAG_DEFAULT = {
                   'gender':'male',
            'accessories':{
                           'neck':{
                                   'type':None,
                                   'color':'black'
                                   },
                           'necklaces':None
                           },
            'equipment':None,
            'cape':{
                    'type':None,
                    'color':'black'
                    },
            'body':{
                    'type':'light',
                    'ears':{
                            'type':'big',
                            'color':'light',
                            },
                    'eyes':'blue',
                    'nose':{
                            'type':'big',
                            'color':'light'
                            }
                    },
            'belt':{
                    'type':None,
                    'colors':'leather'
                    },
            'facial':{
                      'style':None,
                      'color':'black'
                      },
            'feet':{
                    'type':None,
                    'color':'golden'
                    },
            'formal':None,
            'hair':{
                    'style':None,
                    'color':'black'
                    },
            'hands':{
                     'bracelets':None,
                     'bracers':None,
                     'gloves':None
                     },
            'head':{
                    'bandanas':None,
                    'caps':None,
                    'helms':None,
                    'hoods':None,
                    'tiaras':None,
                    },
            'legs':{
                    'armour':None,
                    'pants':None,
                    'skirt':None
                    },
            'torso':{
                     'wings':None,
                     'chain':None,
                     'corset':None,
                     'dress':None,
                     'tightdress':None,
                     'general':{
                                'type':None,
                                'material':'gold'
                                },
                     'robes':None,
                     'shirts':{
                               'type':None,
                               'color':'brown'
                               },
                     'tunics':None,
                     },
            'weapons':{
                       'both hands':None,
                       'left hand':None,
                       'right hand':None
                       }
                   }
        
    def __init__(self, **settings):
        self.settings = SpriteSheetTag.initSettings(SpriteSheetTag.TAG_DEFAULT, settings)
        
        
    @staticmethod
    def initSettings(branch, settings):
        for key in settings.keys():
            if key in branch:
                if settings[key] is None or isinstance(settings[key], str):
                    branch[key] = settings[key]
                elif isinstance(settings[key], dict) and isinstance(branch[key], dict):
                    branch[key] = SpriteSheetTag.initSettings(branch[key], settings[key])
                else:
                    raise TypeError
            else:
                raise AttributeError
        return branch
            
class SpriteSheetHandler():
    def __init__(self):
        self.sheets = []