# --------------------  kwargs in function ------------------------------------------------------
# this allows you to pass a variable number of keyword arguments to a function.

# example of kwargs in function -----------------
def show(**info): 
    for key, value in info.items(): #keys() method returns a view object that displays a list of all the keys in the dictionary. items() method returns a view object that displays a list of dictionary's key-value tuple pairs. 
        print(f"{key}: {value}")
show(name="Lisa", age=22, city="New York")
# output: 
# name: Lisa
# age: 22R
# city: New York