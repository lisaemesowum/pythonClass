# Functions 
# a function is a block of code that performs a specfic task. it helps to define large programs into smaller and  reusable parts. it also helps to reuse code and improve readability.

#------------------------- why function ==========================================
# 1: it makes code organized and easy to understand.
# 2: promotes code reusability.
# 3: reduces repetitions.
# 4: improves debugging and maintenance.
# =====================syntax of function ==========================================

# def function_name(parameters):
#     # function body
#      statement(s)
# return value
# ======================end ==================================================

#  ---------  TYPE OF FUNCTION ---------------------
# -- 1: Built-in function
#    THIS FUNCTIONS A BUILT IN TO PYTHON AND CAN BE USED WITHOUT ANY IMPORT STATEMENT.
#   EXAMPLE: print(), len(), input(), type(),max(), min(), sum() etc.

#  -- 2: User defined function
#   THIS FUNCTIONS ARE CREATED BY THE USER USING def KEYWORD. THEY CAN BE CALLED MULTIPLE TIMES IN THE PROGRAM.
#   EXAMPLE:

def addTwoNumbers(a,b):
    return a + b
sum = addTwoNumbers(5, 10)
print("The sum of 5 and 10 is:", sum)
#  or
print(f"Sum = {sum}")
# ------------------------------------------------------


# -------- no return statement function ----------------
def greet():
    print("You are welcome to Aptech Port Harcourt")
    
greet() 
# ------------------------------------------------------


# -------------- function with default argument ----------------

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

# ----------------- variable length arguments -------------------------------
# this allows you to pass a variable number of arguments to a function. 
# it accept multiple arguments and treat them as a tuple. it is denoted by *args in the function definition.

def total(*nums): # the * before nums indicates that it can accept a variable number of arguments and treat them as a tuple.
    sum_of_num = 0
    
    for n in nums:
        sum_of_num += n
        
    return sum_of_num
print(total(1, 2, 3, 4, 5)) # output: 15
# ----------------------------------------------------------------------------

