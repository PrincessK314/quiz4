from typing import Protocol

class Pet (Protocol):
    def setBirthDate(self, year: int):
        pass

    def getAge(self) -> str:
        pass

class Cat:
    def setBirthDate(self, year: int):
        self.birthYear = year

    def getAge(self) -> str:
        return ("Age: " + str(2024 - self.birthYear) + " years old")
    
class Dog:
    def setBirthDate(self, year: int):
        self.birthYear = year

    def getAge(self) -> str:
        age = 2024 - self.birthYear
        return ("Age: " + str(age) + " years old, or " + str(age*7) + " in dog years")
    

dog :Pet = Dog()
dog.setBirthDate(2020)
print(dog.getAge())