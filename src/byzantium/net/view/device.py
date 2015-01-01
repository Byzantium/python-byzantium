
class Device:
    """ Goals 
        list and set IP,netmask,gateway,mode,state,bssid,essid
        check ability to perform the above
    """

    def __init__(self):
        pass

    def can(self, **abilities):
        """ is able to do or have done to it certian actions """
        pass

    def has(self, **attrs):
        """ has particular properties """
        pass

    def set(self, attr, value):
        """ set attribute """
        pass

    def get(self, attr, default=None):
        """ get attribute """
        pass
