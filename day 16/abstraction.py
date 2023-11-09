from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self,app):
        pass
    def run(self,app):
        self.process(app)

class Laptop(computer):
    def process(self, app):
        print(f"{app} is running in laptop")

class Mobile(computer):
    def process(self, app):
        print(f"{app} is running in Mobile")

laptop= Laptop()
laptop.run("facebook")  

mobile=Mobile()
mobile.run("Mobile Legend")

#inheritance example
#abstraction another example bike
                

