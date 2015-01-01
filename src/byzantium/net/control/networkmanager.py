
from ..NetworkManager_h import *
from . import manager

class NetworkManager(manager.Manager):
    """ Goals 
        list devices given certain criteria
        configure specified devices
        maintain those configs
    """

    def __init__(self):
        """ load up management api """
        bus = dbus.SystemBus()
        proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
        self.nm = dbus.Interface(proxy, "org.freedesktop.NetworkManager")

    def confugure_devices(self, *devices, check=False):
        """ configure all `*devices` 
        return  tuple of bools. True for successes and False for failures.
        """
        pass

    def configure_device(self, device, check=False):
        """ configure device """
        pass

    def get_devices(self, *types):
        """ get a list of all devices, or just those of the type specified """
        pass

    def get_device(self, id):
        pass

    def check_permissions(self):
        """ Check to see what we can do in general
        docs: .GetPermissions ( )
        """
        pass

