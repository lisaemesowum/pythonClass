#Variables for storing data in a computers memory
#eg
aptech_schooling = 2.4
# print(aptech_schooling)

# floating point number
rating = 4.99

# boolen
is_aptech_good = True

# string 
school_name = "APTECH"

course_name = "SE"

#========================================== STRING =================================================================================

course = "Python Programming"

# ------------------------function is a reusable piece of code that carries out a task ------------------------------------------

# len length of a string in python

len(course)               # number of characters
print(len(course))
# get the first character
print(course[0])          #first
print(course[-1])         #the last character

# slice strings  ==============================================
print(course[0:3])        # getting the index of 0 - 3 

first = "Lisa"
last = "Emesowum"
middle_name = "Amarachi"
ful = f"{first} {last} {middle_name}"
# printing the full name 
print(first,last,middle_name) 
# print(ful)
# check how many the names are
# print(len(first,last,middle_name)) # len() takes exactly one argument (3 given))
print(len(ful))

# making Amarachi Emesowum Lisa
print(middle_name,last,first)
# print(reversed(ful)) # this will reverse the string but it will not print it in reverse order
print(ful[::-1]) # this will reverse the string and print it in reverse order






