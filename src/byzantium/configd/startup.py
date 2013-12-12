#!/usr/bin/python

# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

""" startup.py
"""
__authors__ = ['haxwithaxe me@haxwithaxe.net']
__license__ = 'GPLv3'

# Imports
import sys
from .. import *
from . import *

defaults = conf('will_it_mesh.conf')
logger = defaults.utils.get_logger('will_it_mesh')

def on_startup(args):
    """ Entry point of script.
    @param  args    List of arguments passed to the script
    """
    excludes = []
    # eventually grab values from the commandline args here
    # this throws exceptions if it doesn't find anything
    wireless = NetworkDeviceList.wireless(exclude=excludes)
    # set our little state token
    congiured_mesh = False
    # walk through all the interfaces until we find a working one or run out
    for intface in wireless:
        mesh = iface.MeshIFace(intface)
        if mesh.configure():
            congiured_mesh = True
            break
        # else continue to the next and try there
    # if nothing is configured stop here
    logger.warn("No interfaces configured. Exiting.")
    if not configured_mesh: return None
    # else load up the mesh interface
    mesh.load()
    # and setup the client interface.
    client = iface.ClientIFace(mesh.device, client_number)
    client.load()
    # add the commotion-wireless route
    mesh.add_commotion_route()
    # Start the captive portal daemon on the client interface.
    client.start_captive_portal()
    logger.info("Started captive portal daemon.")
    # Make some config files
    client.make_hosts_file()
    dnsmasq = rc.DNSMasq(mesh, client)
    dnsmasq.make_include()
    # Poke some services we changed configs for
    dnsmasq.rc(action="restart")
    olsrd = rc.OLSRD(mesh)
