# 4:  recursive function 

# this is a function that calls itself in order to solve a problem. it is used to solve problems that can be broken down into smaller subproblems.
# it is important to have a base case to prevent infinite recursion.

def factorial(n):
    if n <= 2:
        return n
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) # output: 120

# -------------------  explain the above code
# the above code defines a recursive function called factorial that calculates the factorial of a given number n.
# the function checks if n is less than or equal to 2, in which case it returns n (since the factorial of 0 is 1, 
# the factorial of 1 is 1, and the factorial of 2 is 2).
# if n is greater than 2, the function returns n multiplied by the result of calling factorial with n - 1. 
# This continues until the base case is reached, at which point the function starts returning values and calculating the final result. 
