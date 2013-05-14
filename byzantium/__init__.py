# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

BYZANTIUM_CONSTANTS = 'opt/byzantium/byzantium_const.conf' #'/opt/byzantium/byzantium_const.conf'

def mknum(value, _type, base=10):
    try:
        value = _type(value, base)
    except:
        pass
    return value

def convert2type(value):
    if not value or len(value) < 2: return value
    if value.startswith('(list)'):
        value = value.replace('(list)','', 1)
        sep = value.pop(0)
        return [convert2type(x) for x in value.split(sep)]
    elif value.startswith('(float)'):
        return mknum(value.replace('(float)','', 1), float)
    elif value.startswith('(int)'):
        return mknum(value.replace('(int)','', 1), int)
    elif value.strip().lower() == 'true':
        return True
    elif value.strip().lower() == 'false':
        return False
    elif value.startswith('(none)') or value.startswith('(null)') or value.startswith('(noop)'):
        return None
    else:
        return value

class Const:
    def __init__(self):
        self.config = {}
        self.load()
        print(self.config)

    def get(self, *keys, **kwargs):
        print('const.get()', keys, kwargs)
        if 'default' in kwargs:
            default = kwargs['default']
        else:
            default = None
        item = None
        depth = len(keys)
        tmp_config = self.config.copy()
        depth = 0
        for i in keys:
            if i in tmp_config:
                tmp_config = tmp_config[i]
            elif depth == 0:
                return default
            depth += 1
        return tmp_config

    def load(self):
        '''Load all sections of an ini file as a list of dictionaries'''
        constants_conf = os.path.join(os.getcwd(), BYZANTIUM_CONSTANTS)
        conpar = configparser.SafeConfigParser()
        conpar.read(constants_conf)
        print(constants_conf)
        print(os.path.exists(constants_conf))
        print(conpar.sections())
        self.config = {}
        for sec in conpar.sections():
            if sec == 'main':
                for k,v in conpar.items(sec):
                    self.config[k] = convert2type(v)
            else:
                self.config[sec] = {}
                for k,v in conpar.items(sec):
                    self.config[sec][k] = convert2type(v)
        return self.config

const = Const().load()

__all__ = ['avahi','const', 'config', 'utils']

