# ---------------function is a reusable piece of code that carries out a task ------------------------------------------
course = "Python Programming"
print(course.upper()) # convert to upper case
print(course.lower()) #lower case
print(course.title()) #capitalized the first letter of the text
print(course.strip()) # remove white space
print(course.lstrip()) #remove the left side space
# get the index of a character
print(course.find("Pro"))
# replace the text
print(course.replace("P", "L"))
# check the existience of a character // returns boolen
print("Pro" in course) #experssion is a piece ofcode that produces a value 
# Not to check if it contains the character
print("lisa" not in course)