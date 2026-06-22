Student = {
  "name": "Lisa", 
  "age": 16, 
  "gender": "female"
}

search_name = "Lisa"
if search_name not in Student.values():
    print("not found")
else:
    print(Student)

print(Student["name"])