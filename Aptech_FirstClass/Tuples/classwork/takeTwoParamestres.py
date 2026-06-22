# write a python program that takes two paramesters and return 
# addition
# substraction
# multipication
# modules

def twoParamesters(a,b):
    add = a + b
    diff = a - b
    multi = a * b
    molule = a % b
    return add , diff , multi , molule
print(twoParamesters(10,20))