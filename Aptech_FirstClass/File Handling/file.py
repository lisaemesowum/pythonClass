# How to read a file 

file = open("Aptech_FirstClass/File Handling/Student.txt")
content = file.read()

print(content.split("\n"))

# type of the file
# print(type(content)) 

# read only the file line

print(file.newlines) 

file.close()

#------------------------- Read the greet file  -----------------------------

file = open("Aptech_FirstClass/File Handling/greet.txt")
print(file.read(5)) # the length of the value, you want to print out 


# -------------- close a file ---------------------

# after reading, you now close it the good method

with open("Aptech_FirstClass/File Handling/Student.txt","r") as file:
    content = file.read()
    print(content)