Student = {
  "student1": {
    "name": "lisa",
    "age": 12,
    "gender": "Female",
    "courses": ["python", "Java"]
  },
  "student2": {
    "name": "David",
    "age": 23,
    "gender": "Male",
    "courses": ["python", "Java"]
  }
}

# 1. Works perfectly
print(Student["student1"]["name"])

# 2. FIXED: Changed "course" to "courses"
print(Student["student1"]["courses"][0])

# 3. FIXED: Changed index 0 to the actual key "student2"
print(Student["student2"]["name"])
