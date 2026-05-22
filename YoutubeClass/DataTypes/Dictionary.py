#Distionary are  collection like the list but is unorderd chnageable and indexed

# example

courses = { 1: "java",
            2:"python",
            3:"machine learning"
           }
print(courses)

# to get a value
print(courses.get(1))

# update the value of 1
courses[1] = "book"
print(courses)