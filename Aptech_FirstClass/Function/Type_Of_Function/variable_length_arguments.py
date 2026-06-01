# ----------------- variable length arguments -------------------------------

# this allows you to pass a variable number of arguments to a function. 
# it accept multiple arguments and treat them as a tuple. it is denoted by *args in the function definition.

def total(*nums): # the * before nums indicates that it can accept a variable number of arguments and treat them as a tuple.
    sum_of_num = 0
    
    for n in nums:
        sum_of_num += n
        
    return sum_of_num
print(total(1, 2, 3, 4, 5)) # output: 15