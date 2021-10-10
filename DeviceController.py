import yaml
from DeviceTypes import DeviceTypes
from threading import Thread

class DeviceControllerException(Exception):
    pass

class DeviceController:
    def __init__(self, config_yaml_file):
        #lable -> device relation
        self.devices = {}
        #name -> label relation
        self.names = {}

        self.device_workers = []
        config_yaml = None
        with open(config_yaml_file, "r") as yamlstream:
            config_yaml = yaml.safe_load(config_yaml_file)
        self.load_config(config_yaml)


    def load_config(self, config_yaml)
        for device_yaml in config_yaml["devices"]:
            items = list(device_yaml.items())
            self.register_device(items[0], items[1])

    def load_device(self, device_type, device_config):
        this_device = DeviceTypes[device_type]()
        this_device.initialize_config(device_config)
        self.register_device(this_device)

    def register_device(self, device):
        if device.label in self.devices or device.label in self.names:
            raise DeviceControllerException(f"Cannot register device - label '{device.label}' allready registered.")
        if device.name in self.devices or device.name in self.names:
            raise DeviceControllerException(f"Cannot register device - label '{device.name}' allready registered.")

        self.devices[device.label] = device
        self.names[device.name] = device.label

    def do(self, label, device_fx, args):
        bound_fx = device_fx.__get__(self.devices[label], self.devices[label].__class__)
        setattr(self.devices[label],device_fx.__name__,bound_fx)
        worker = Thread(target=bound_fx, args=args)
        worker.start()
        self.device_workers.append(worker)

        


    def do_name(self, name, device_fx, args):
        return self.do(self.names[name], device_fx, args)

    def initiate(self):

    def control_loop(self):
        for w in workers:
            if not w.is_alive()


    def start(self):
        self.control_running = True
        start_control_loop()


    def stop(self):

        