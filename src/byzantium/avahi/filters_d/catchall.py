# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

from byzantium.avahi.filter import AvahiFilter
import re

class Filter(AvahiFilter):
    """ Match all byzantium service types """
    byz_tcp = re.compile('[\w.-]*__byz__\._tcp')
    byz_udp = re.compile('[\w.-]*__byz__\._udp')
    def match(self, record, action=None):
        """ Match every record for a byzantium service
        @param  record      Record object to inspect
        @param  action      action to take based on match
        """
        if byz_tcp.match(record.service_type) or byz_tcp.match(record.service_type):
            return True
        else:
            return False
