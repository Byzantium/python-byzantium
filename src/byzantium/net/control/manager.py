
class Manager:
    """ Goals 
        list devices given certain criteria
        configure specified devices
        maintain those configs
    """

    def __init__(self):
        """ load up management api """
        pass

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
        """ get an individual device by it's name """
        pass

    def check_permissions(self):
        """ Check to see what we can do in general
        docs: .GetPermissions ( )
        """
        pass

