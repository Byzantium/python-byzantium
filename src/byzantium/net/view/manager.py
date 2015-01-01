
class Manager:
    """ Goals 
        find usable devices
        configure them as mesh/AP/gateway interfaces
        maintain those configs
    """

    def __init__(self, control):
        """ load up management api """
        self.control = control

    def find_mesh_able(self):
        """ find devices that can be used for mesh networking """
        self.find_devices(mode='adhoc',type='wireless')
        pass

    def find_ap_able(self):
        """ find devices that can be used in AP mode """
        self.find_devices(mode='ap',type='wireless')
        pass

    def find_gateways(self):
        """ find devices with global gateway """
        self.find_devices(gateway='0.0.0.0')
        pass

    def find_devices(self, **params):
        """ find devices based on parameters """
        matching_devices = []
        devices = control.get_devices(type=params.get('type', 'all'))
        for device in devices:
            if device.can(**params):
                matching_devices.append(device)
        return matching_devices

    def configure_mesh(self, *devices):
        """ configure devices passed as mesh devices """
        pass

    def configure_captive_portal(self, *devices):
        """ configure devices passed under the captive portal """
        pass

    def configure_ap(self, *devices):
        """ configure the devices passed as Access Points """
        pass

    def configure_gateway(self, *devices):
        """ configure the devices passed as gateway interfaces (based on their gateway not necessarily 0.0.0.0) """
        pass

