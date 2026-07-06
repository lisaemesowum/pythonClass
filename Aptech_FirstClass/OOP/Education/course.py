class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        # add student to the course
        # make list of student
        self.Student = []
        
    def add_student(self, student):
        if len(self.Student) < self.max_students:
            self.Student.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for Student in self.Student:
            value += Student.get_grade()
        return value / len(self.Student)
    
