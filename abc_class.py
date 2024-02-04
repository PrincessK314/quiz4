from abc import ABC, abstractmethod

class Pet (ABC):
    @abstractmethod
    def setBirthDate(self, year: int):
        pass

    @abstractmethod
    def getAge(self) -> str:
        pass

class Cat (Pet):
    def setBirthDate(self, year: int):
        self.birthYear = year

    def getAge(self) -> str:
        return ("Age: " + str(2024 - self.birthYear) + " years old")
    
class Dog (Pet):
    def setBirthDate(self, year: int):
        self.birthYear = year

    def getAge(self) -> str:
        age = 2024 - self.birthYear
        return ("Age: " + str(age) + " years old, or " + str(age*7) + " in dog years")
    

cat = Cat()
cat.setBirthDate(2020)
print(cat.getAge())