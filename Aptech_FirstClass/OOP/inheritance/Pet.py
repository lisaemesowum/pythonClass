
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")
        

p = Pet("Tim",19)
p.show()
