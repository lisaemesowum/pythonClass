# A Local variable is a variable that is defined inside a function and can only be accessed within that function.
# example of local variable --------------------
def my_function2():
    local_var = "I am a local variable"
    print(local_var) # this will print the local variable
my_function2() # output: I am a local variable

# trying to access local variable outside the function will result in an error
# print(local_var) # this will raise a NameError