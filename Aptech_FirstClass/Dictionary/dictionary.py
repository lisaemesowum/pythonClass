# creating a dictionary
Student = {
  "name": "Lisa", 
  "age": 16, 
  "gender": "female"
}
print(Student)


# student = dict()

# --- accessing the value --------------------------------------
print(Student["name"])

# -- modify the age to 20 --------------------------------------
Student["age"] = 20
print(Student)

# remove in dictionary
Student.pop("age")
print(Student)
# use the delete key word
del Student["name"]
print(Student)

# check if a particular key exist
print("name" in Student)

# get 
print(Student.get("firstName","Not found"))

     
