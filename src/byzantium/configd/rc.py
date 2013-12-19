#!/usr/bin/python

# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

"""
RC script-like class and subclasses for byzantium_configd.py

ChangeLog
- 2013/10/14 - haxwithaxe - seperated interface classes from the main code.
"""
__authors__ = ['haxwithaxe me@haxwithaxe.net']
__license__ = 'GPLv3'

# Imports
import byzantium

logger = byzantium.utils.Utils().get_logger('rc')

class RC:
    cmd = []

    def status(self):
        return True

    def rc(self, action="restart"):
        """ Poke at dnsmasq. 
        @param  action      String, parameter to pass to /etc/rc.d/rc.dnsmasq. It must be valid as per that script's requirements.
        @return             Return value of '/etc/rc.d/rc.dnsmasq'
        """
        logger.info("%s dnsmasq." % action.upper())
        self.cmd.append(action.lower())
        return shell(self.cmd)
    
class DNSMasq(RC):
    def __init__(self, mesh ,client):
        self.mesh = mesh
        self.client = client

    def make_include(self):
        """ Generate an /etc/dnsmasq.conf.include file.
        """
        prefix = '.'.join(client.ipv4.split('.')[:3])
        ipv4_template = "%s.%d"
        start = ipv4_template % (prefix, 2)
        end = ipv4_template % (prefix, 254)
        dhcp_range = "dhcp-range=%s,%s,5m" % (start, end)
        include_file = open(defaults.get("files", "dnsmasq-include"), 'w')
        include_file.write(dhcp_range)
        include_file.close()

    def rc(self, action="restart"):
        """ Poke at dnsmasq. 
        @param  action      String, parameter to pass to /etc/rc.d/rc.dnsmasq. It must be valid as per that script's requirements.
        @return             Return value of '/etc/rc.d/rc.dnsmasq'
        """
        logger.info("%s dnsmasq." % action.upper())
        self.cmd.append(action.lower())
        return shell(self.cmd)

class OLSRD(RC):
    def __init__(self, mesh):
        self.mesh = mesh

    def _start(self):
        """ Start olsrd.
        @return             Return value of '/usr/sbin/olsrd'
        """
        logger.info("Starting routing daemon.")
        return shell('/usr/sbin/olsrd', '-i', self.mesh.device)

    def _stop(self):
        """
        Stop OLSRD
        @return             Return value of 'killall -w olsrd'
        """
        return shell('/bin/killall', '-w', 'olsrd')

    def _restart(self):
        if self._stop() == 0:
            logger.info("Stopping routing daemon.")
            if self._start() == 0:
                logger.info("Starting routing daemon.")
            else:
                logger.info("Failed to start routing daemon.")
        else:
            logger.info("Failed to stop routing daemon.")

    def rc(self, action="restart"):
        switch = { 'start':   self._start,
                   'stop':    self._stop,
                   'restart': self._restart,
                   'status':  self._status }
        try:
            switch[action.lower()]()
        except KeyError:
            raise Exception(action + " is not a valid option")


