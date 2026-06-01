# -------------- function with default argument ----------------

# this allows you to specify a default value for a parameter in case the caller does not provide a value for that parameter.
# it is denoted by assigning a value to the parameter in the function definition.

def greet2(name= "Lisa"):
    return f"Hello {name}, you are welcome to Apptech Port Harcourt"

print(greet2("John")) # using default argument
# it overrides the default argument with the provided argument
# -------------------------------------------------------------- 

# write a function to calculate a area of a rectangle
# to calculate the area of a rectangle
# how long is the length and width of the rectangle
# formula 
# area = length * widths
# or A = i x w 
def areaOfRectangle(length, width):
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = areaOfRectangle(length, width)
print(f"The area of the rectangle is: {area}")
# -------------------------------------------------------------- 
