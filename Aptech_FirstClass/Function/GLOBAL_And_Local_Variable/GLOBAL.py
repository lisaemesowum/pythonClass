# A Global variable is a variable that is defined outside of any function and can be accessed from anywhere in the program.
# example of global variable -------------------

global_var = "I am a global variable"
def my_function():
    print(global_var) # this will print the global variable
my_function() # output: I am a global variable
