from abc import ABC,abstractmethod

class Bike(ABC):
    @abstractmethod
    def process(self,name):
        pass
    def run(self,name):
        self.process(name)

class MT(Bike):
    def process(self, name):
        print(f"I am buying {name} bike ")

class Royal_Enfield(Bike):
    def process(self, name):
        print(f"{name} has classic look")

mt= MT()
mt.run("MT-15")  

royal=Royal_Enfield()
royal.run("Bullet")
  
                

