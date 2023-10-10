from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def accelarate(self):
        pass
class Swift(Car):
    def start(self):
        print("swift start")
    def stop(self):
        print("swift stop")
    def accelarate(self):
        print("swift accelarate")
obj=Swift()
obj.start()
obj.stop()
obj.accelarate()
