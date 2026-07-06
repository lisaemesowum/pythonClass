import Student 
import course
s1 = Student.Student("Lisa", 19,98)
s2 = Student.Student("Emesowum", 20, 75)
s3 = Student.Student("John", 21, 65)
course = course.Course("Python", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.Student[0].name)  # Output: Lisa

# get average grade of the course
print(course.get_average_grade())