# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

import os
import logging
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

__license__ = 'GPL v3'

__author__ = 'haxwithaxe me@haxwithaxe.net'

BYZANTIUM_CONSTANTS = os.environ.get('BYZANTIUM_CONST', '/opt/byzantium/byzantium_const.conf')


class Const:
    def __init__(self):
        self.config = {}
        self.load()
        logging.debug(str(repr(self.config)))

    def get(self, *keys, **kwargs):
        logging.debug( str(('const.get()', keys, kwargs)) )
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
        if not os.path.exists(constants_conf): raise Exception(constants_conf+' Not found.')
        conpar.read(constants_conf)
        logging.debug(constants_conf)
        logging.debug(os.path.exists(constants_conf))
        logging.debug(conpar.sections())
        self.config = {}
        for sec in conpar.sections():
            if sec == 'main':
                for k,v in conpar.items(sec):
                    self.config[k] = convert_to_type(v)
            else:
                self.config[sec] = {}
                for k,v in conpar.items(sec):
                    self.config[sec][k] = convert_to_type(v)
        return self.config

