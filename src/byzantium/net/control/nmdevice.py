
from ..NetworkManager_h import *
from . import device

class NMDevice(device.Device):

    def extract_properties(self, device_obj):
        dev_proxy = bus.get_object("org.freedesktop.NetworkManager", device_obj)
        prop_iface = dbus.Interface(dev_proxy, "org.freedesktop.DBus.Properties")
        return prop_iface.GetAll("org.freedesktop.NetworkManager.Device")

    def device_type(self):
        """ return the device type """
        return NMDeviceType.get(self.props.get('DeviceType'), "Unknown")

    def state(self):
        """ return the state of the device """
        return NMDeviceState.get(self.props.get('State'), "Unknown")

    def get(self, attr, default=None):
        pass

    def add(self, attr, value):
        pass

