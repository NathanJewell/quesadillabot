

class DeviceException(Exception):
    pass

class Device:

    def __init__( self):
        pass

    
    #validate configuration params for device
    #@abstractmethod
    def initialize_config(self, config):
        self
        #extract variables from config and pass to initialize


    #@abstractmethod
    def initialize(self, *params):
        pass
        #initialize class variables on device