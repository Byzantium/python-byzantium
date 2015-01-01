
class Device:

    def __init__(self, device_obj):
        """  take the device object from the manager and extract the properties """
        self.props = self.extract_properties(device_obj
                
    def extract_properties(self, dev):
        """ extract the device properties from the managment and return as a dict """
        pass

    def device_type(self):
        """ return the device type """
        pass

    def state(self):
        """ return the state of the device """
        pass

    def get(self, attr, default=None):
        """ get attribute of this device and return default if the attr doesn't exist """
        pass

    def add(self, attr, value):
        """ set attribute of this device to value """
        pass

