# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

import os
from collections import Sequence
from ..utils import Utils
from ..config import Config
from .. import const

EOF = '\00' #FIXME replace with something sensable before release
EOB = '\n\n' #FIXME replace with something sensable before release

logger = Utils().get_logger(name='ServiceIndex', new=True)
config = Config('service_index.conf')

class ByzTxtItem:
    """ txt record entry object with byzantium specific format """

    def __init__(self, parent, key, lookup, lookup_default=None, value=None, multiline=False):
        """
        @param  parent
        @param  key
        @param  lookup
        @param  lookup_default
        @param  value
        @param  multiline
        """
        self.parent = parent
        self.key = key
        self.lookup = lookup
        self.lookup_default = lookup_default
        self.value = value
        self.parent.ns[self.get_format()] = self
        self._multiline = multiline

    def __call__(self):
        """ Return the entry value when called """
        return self.value

    def set(self, value):
        """ For the sake of conformity
        @param  value   The content of the txt record entry
        """
        self.value = value

    def get(self, key=None):
        """ For the sake of conformity
        @param  key     The key of the txt record entry (not used to retrieve the value)
        @return         The entry value
        """
        return self.value

    def append(self, line):
        """ Append a line to the entry.
        If multiline is set to False this is a no-op.
        @param  line    line of text for the txt record entry
        """
        if self._multiline:
            self.value = '\n'.join([self.value, value])
    
    def get_format(self):
        """ Return the FIXME ... wtf format is this """
        return config.get(self.lookup, default=self.lookup_default)

class ByzTxt:
    ''' Class to mangle the txt element of avahi records with certian formatting '''

    def __init__(self, txt_record=None):
        logger.debug('txt: %s' % txt_record)
        logger.debug('ByzTxt.__init__')
        self.orig = txt_record
        self.ns = {}
        ByzTxtItem(self, 'show', 'show-service-to-key', 'show')
        ByzTxtItem(self, 'description', 'service-description-key', 'description')
        ByzTxtItem(self, 'append_to_url', 'append-string-post-port-key', 'appendtourl')
        ByzTxtItem(self, 'ground_station_address', 'groundstation-addr', 'groundstation-addr') # not implemented
        ByzTxtItem(self, 'pgp_id', 'pgp-id', 'pgp-id') # not implemented
        ByzTxtItem(self, 'pgp_pubkey', 'pgp-pubkey', 'pgp-pubkey') # not implemented
        if self.orig: self.__parse()

    def to_dict(self):
        d = {}
        for lookup, obj in self.ns.items():
            d.update({obj.key:obj.get()})
        return d

    def __get_key_val_pair(self, line, sep='='):
        key, val = (line+sep).strip().split(sep,1)
        val_list = [x for x in val]
        val_list.pop()
        val = ''.join(val_list)
        return key, val

    def __parse(self):
        logger.debug('ByzTxt.__parse')
        desc_list = []  # accumulator for the multi-line description
        collect_until_next = None  # container to collect lines until another key is found (or EOF).
        for line in self.orig.strip().split('\n'):
            logger.debug('line: %s' % line)
            key,val = self.__get_key_val_pair(line)
            val = val.replace('\r','').replace('\n', '')
            # if key is a defined key, then make sure collect_until_next is set to None
            if key in self.ns:
                collect_until_next = key
                self.ns[key].set(val)
            elif line in (EOB,EOF): # if block is an end of block or end of 'file' (end of the entire txt record)
                collect_until_next = None
            elif collect_until_next:
                # the append method will handle whether or not to actually
                #append on it's own
                self.ns[collect_until_next].append(line)

class Record:
    """ Avahi service record """

    def __init__(self, **kwargs):
        """ FIXME specify possible values of kwargs
        @param fullname
        @param interface
        @param protocol
        @param service_name
        @param service_type
        @param service_domain
        @param hostname
        @param ip_version
        @param ipaddr
        @param port
        @param txt
        @param flags
        """
        logger.debug('Record.__init__')
        self.ns = ['fullname','interface', 'protocol', 'service_name', 'service_type', 'service_domain', 'hostname', 'ip_version', 'ipaddr', 'port', 'txt', 'flags']
        self.fullname = None
        self.interface = kwargs.get('interface')
        self.protocol = kwargs.get('protocol')
        self.service_name = kwargs.get('service_name')
        self.service_type = kwargs.get('service_type')
        self.service_domain = kwargs.get('service_domain')
        self.hostname = kwargs.get('hostname')
        self.ip_version = kwargs.get('ip_version')
        self.ipaddr = kwargs.get('ipaddr')
        self.port = kwargs.get('port')
        self.txt = kwargs.get('txt')
        self.flags = kwargs.get('flags')
        self.set_fullname()
        self.byz_txt = None
        if self.txt:
            self.byz_txt = ByzTxt(self.txt)

    def to_dict(self):
        """ Return this record as a dict
        @return         dict of values in this record
        """
        logger.debug('Record.to_dict')
        d = {}
        for key in self.ns:
            if key in self.__dict__:
                d.update({key: self.__dict__[key]})
        for key, val in self.byz_txt.to_dict().items():
            if key in d:
                altkey = 'txt_%s' % key
                logger.warn('changed dictionary key `%s` to `%s`' % (key, altkey))
                key = altkey
            d.update({key:val})
        logger.debug('Record.to_dict: %s' % str(repr(d)) )
        return d

    def set_fullname(self):
        """ Set 'fullname' used as a unique id and required by on of the callbacks """
        logger.debug('Record.set_fullname')
        if self.service_name and self.service_type and self.service_domain:
            self.fullname = '%s.%s%s' % (self.service_name, self.service_type,self.service_domain)
            logger.debug('Record.set_fullname: %s' % self.fullname)

    def from_signal(self, signal, args):
        """ Load the record from an avahi record """
        logger.debug('Record.from_signal')
        argc = len(args)
        if signal in ('ItemNew','ItemRemove', 'Found'):
            self.interface = args[0]
            self.protocol = args[1]
            self.name = args[2]
            self.service_type = args[3]
            self.service_domain = args[4]
            # If this is called from a ResolveService callback
            #set the extra bits it has that we just set to None.
            if signal == 'Found':
                self.hostname = args[5]
                self.ip_version = args[6]
                self.ipaddr = args[7]
                self.port = args[8]
                self.txt = args[9]
                self.flags = args[10]
                self.byz_txt = ByzTxt(self.txt, self.config)
                self.description = self.byz_txt.description
                self.append_to_url = self.byz_txt.append_to_url
            else:
                self.flags = args[5]
        self.set_fullname()


class ServiceIndex:
    """ Index of services on the network """
    def __init__(self):
        """ FIXME describe setup of the object """
        logger.debug('ServiceIndex.__init__')
        config_file =  config.get('service-index')
        if not config_file: raise Exception('Missing service-index entry in service-index.conf')
        self.__file = config.get('service-index')
        self.utils = Utils()
        self._index = {}

    def dump(self):
        """ get the whole index """
        logger.debug('ServiceIndex.dump')
        logger.debug(repr(self._index))
        return self._index

    def get(self, **attribs):
        """ If an attrib is set to '*' it will match any record with the
        attribute regardless of it's value """
        keyword = None
        if attribs and len(attribs) > 0:
            if KEYWORD in attribs: keyword = attribs[KEYWORD]
            index = {}
            for rid, record in self._index.items():
                for k, v in attribs.items():
                    if keyword and str(record[k]).contains(keyword):
                        index[rid] = record
                        break   # matched keyword in one attrib now move to next record
                    elif k in record:
                        if v == '*' or v == record[k]:
                            index[rid] = record
                            break   # matched one attrib now move to next record
            return index
        else:
            return self._index

    def _write(self):
        """ Write the index to an ini file """
        logger.debug('ServiceIndex._write')
        self.utils.dict2ini(self._index, self.__file, convert=True)

    def _read(self):
        """ Load the index from an ini file """
        logger.debug('ServiceIndex._read')
        if self.__file and os.path.exists(self.__file):
            self._index = self.utils.ini2dict(self.__file, convert=True)

    def _wipe(self):
        """ Clear saved and live copies of the index. """
        logger.debug('ServiceIndex._wipe')
        self._index = {}
        self._write()

    def add(self, record):
        """ Add an item to the saved copy of the index (same as update). 
        @param  record      Record object to add to the index.
        """
        logger.debug('ServiceIndex.add')
        self.update(record)

    def update(self, record):
        """ Add an item to the saved copy of the index (same as add). 
        @param  record      Record object to add to the index.
        """
        logger.debug('ServiceIndex.update')
        self._read()
        self._index.update({record.fullname:record.to_dict()})
        self._write()

    def pull(self):
        """ Dump live copy of the index and read the saved one. """
        logger.debug('ServiceIndex.pull')
        self._index = {}
        self._read()

    def push(self):
        """ Write the live copy of the index to disk, overwriting the saved one. """
        logger.debug('ServiceIndex.push')
        self._write()

    def remove(self, key):
        """ Remove item from the saved copy
        @param  key     key of the record in the index to remove.
        """
        logger.debug('ServiceIndex.remove')
        self._read()
        if key in self._index:
            del self._index[key]
        self._write()
