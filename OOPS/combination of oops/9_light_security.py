# 9. Classes:
# • LightDevice
# • SecurityDevice
# • SmartCamera(LightDevice, SecurityDevice)
# Requirements:
# • Resolve method conflicts using MRO
# • Encapsulate internal camera logs
# • SmartCamera overrides both parents’ behaviors
# • Use super() responsibly in multiple inheritance

from abc import ABC, abstractmethod
class LightDevice(ABC):
    @abstractmethod
    def on(self):
        print("turning on light")
        super().on()
    @abstractmethod
    def off(self):
        print("turning off light")
        super().off()
class SecurityDevice(ABC):
    def on(self):
        print("turning on security")
    def off(self):
        print("turning off security")
    @abstractmethod
    def record(self):
        print("security is recording")
    def __logs(self):
        print("security logs showing")
    def show_logs(self):
        if input("Enter password: ")=="1234":
            self.__logs()
class SmartCamera(LightDevice,SecurityDevice):
    def on(self):
        print("turning on camera")
        super().on()
    def off(self):
        print("turning off camera")
        super().off()
    def record(self):
        print("camera is recording")
        super().record()
obj=SmartCamera()
obj.record()
obj.on()
obj.off()
obj.show_logs()