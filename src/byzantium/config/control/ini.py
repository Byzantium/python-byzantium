# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

import os
import logging

class INI:
    ''' Make me read from a file and/or environment'''
    ext = 'ini'

    def ini_to_list(self, filename, convert=False):
        '''Load all sections of an ini file as a list of dictionaries'''
        conpar = configparser.SafeConfigParser()
        conpar.read(filename)
        config = []
        for sec in conpar.sections():
            section = {}
            for k,v in conpar.items(sec):
                section[k] = convert_to_type(v, convert)
        return config

    def ini_to_dict(self, filename, section=None, convert=False):
        '''Load all sections of an ini file as a list of dictionaries'''
        conpar = configparser.SafeConfigParser()
        conpar.read(filename)
        config = {}
        logging.debug('sections %s' % repr(conpar.sections()))
        for sec in conpar.sections():
            logging.debug('sec, conpar.items(sec): %s\n%s' % (sec, repr(conpar.items(sec))))
            config[sec] = {}
            for k,v in conpar.items(sec):
                logging.debug('for k, v in conpar.items(sec): k, v: %s, %s' % (k, v))
                config[sec][k] = convert_to_type(v, convert)
        if section:
            config.update(config[section])
            logging.debug('config.__call__: %s' % repr(config))
        return config

    def dict_to_ini(self, input_dict, filename, convert=False):
        '''Load all sections of an ini file as a list of dictionaries'''
        if not filename: raise Exception('No filename passed to dict2ini(data, filename)')
        conpar = configparser.SafeConfigParser()
        config = input_dict
        for sec in config:
            conpar.add_section(str(sec))
            for k,v in config[sec].items():
                conpar.set(str(sec), str(k), convert_from_type(v, convert))
        with open(filename, 'wb') as inifile:
            conpar.write(inifile)

    def file_to_str(self, file_name, mode = 'r'):
        if not os.path.exists(file_name):
            self.logger.debug('File not found: '+file_name)
            return ''
        fileobj = open(file_name, mode)
        filestr = fileobj.read()
        fileobj.close()
        return filestr

    def file_to_json(self, file_name, mode = 'r'):
        filestr = self.file_to_str(file_name, mode)
        try:
            return_value = json.loads(filestr)
        except ValueError as val_e:
            self.logger.debug(val_e)
            return_value = None
        return return_value

    def str_to_file(self, string, file_name, mode = 'w'):
        fileobj = open(file_name, mode)
        fileobj.write(string)
        fileobj.close()

    def json_to_file(self, jsonobj, file_name, mode = 'w'):
        try:
            string = json.dumps(jsonobj)
            self.str_to_file(string, file_name, mode)
            return True
        except TypeError as type_e:
            self.logger.debug(type_e)
            return False

    def convert_to_type(self, value, convert=True):
        if not convert: return value
        if not value or len(value) < 2: return value
        if value.startswith('(list)'):
            value = value.replace('(list)','', 1)
            sep = value.pop(0)
            return [convert_to_type(x) for x in value.split(sep)]
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

    def convert_from_type(self, value, convert=True):
        if not convert: return value
        vtype = type(value)
        if vtype == list:
            return '(list)[%s]' % ','.join([convert_from_type(x) for x in value.split(sep)])
        elif vtype == float:
            return '(float)%s' % str(value)
        elif vtype == int:
            return '(int)%s' % str(value)
        elif value == True:
            return 'true'
        elif value == False:
            return 'false'
        elif value == None:
            return '(none)'
        else:
            return str(value)
