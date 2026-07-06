
from Aptech_FirstClass.OOP.inheritance import Pet


class Cat(Pet):
    def speak(self):
        print("Meow")


c = Cat("Bill", 34)
c.show()