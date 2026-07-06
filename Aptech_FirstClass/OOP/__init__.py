# The __init__() method is used to assign values to object properties, 
# or to perform operations that are necessary when the object is being created.
class Dog:
    def __init__(self,name,age): 
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
    
d2 = Dog("Tommy", 34)
d2.set_age(23)
print(d2.get_name())
print(d2.get_age())