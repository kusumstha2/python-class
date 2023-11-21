class Person:
    def __init__(self) -> None:
        self.name="Kusum"
        self._age=21
        self.__salary="17k"
     
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        self.__salary = salary

        """ we can also """

person=Person()
person.name="krijal"
print(person.name)
print(person._age)  
 

person.salary="19k"
print(person.salary) 

    