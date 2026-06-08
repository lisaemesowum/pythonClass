"""
earching can refer to checking for an item in a collection
search in List
"""
student = ["Elana","Lisa", "Abbas", "samuel"]

result = "Abbas" in student
if result:
    student.remove("Abbas")
# print("Abbas" in student)
print(student)

# if lisa in not there
# search for tinubu

result = "Tinubu" not in student
print(result)
students = ["Elana","Lisa", "Abbas", "samuel"]

# use this approch
# looping
for student in students:
    if student == "Lisa":
        break
    print(student)

# to know the particular index
for i in range(len(students)):
    print(f"{i}=> {students[i]}")