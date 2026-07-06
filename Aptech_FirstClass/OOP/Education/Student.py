import course 

class Student:
    def __init__(self, name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade


# s1 = Student("Lisa", 19,98)
# s2 = Student("Emesowum", 20, 75)
# s3 = Student("John", 21, 65)
# course = course.Course("Python", 2)