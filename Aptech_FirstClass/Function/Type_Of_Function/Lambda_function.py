# 3: Lambda function

# this is an anonymous function that can have any number of arguments but only one expression. 
# it is denoted by the lambda keyword.

def total(*nums): # the * before nums indicates that it can accept a variable number of arguments and treat them as a tuple.
    sum_of_num = 0
    
    for n in nums:
        sum_of_num += n
        
    return sum_of_num

square = lambda X : X * X
cube = lambda Lisa : Lisa  ** Lisa 
print(cube(5)) # output: 3125
#  explain the above code 
# the above code defines a lambda function called cube that takes one argument Lisa and returns the result of Lisa raised to the power of Lisa. 
# when we call cube(5), it calculates 5 raised to the power of 5, which is 3125.
