# Logical operators
# Used to combine conditional expression

# ----------- list of logical operators -------

# 1: AND (and) RETURNS TRUE IF BOTH THE CONDITION ARE TRUE.IF NOT IT RETURNS FALSE
# --------- EXAMPLE
x = 10
y = 20
z = 30
if x > y and y > z:  #if both are true print 
    print("x is the largest number")
else:
    print("x is not the larget number")

# 2: OR  (or) RETURNS TRUE IF ONE CONDITION IS TRUE , NOT IT WILL RETURN FALSE
# --------- EXAMPLE
x = 10
y = 20
z = 30
if x > y or x > z: 
    print("x is at least larger than one number")
else:
    print("x is  the smallest number")

# 3: NOT (not) Not is unary logical operator
# RETURNS TRUE IF THE CONDITIONAL EXPESSION RETURNS FALSE AND VICE - VERSA.
# --------- EXAMPLE
x = 10
y = 20
z = 30
if not(x > y or x > z):   
    print("x is the largest number")
else:
    print("x is not the smallest number")

