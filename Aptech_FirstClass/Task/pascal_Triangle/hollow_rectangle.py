
    # ***************
    # *             *
    # *             *
    # *             *
    # ***************

# method 1 # Hollow rectangle pattern
rows = 5
column = 15

for i in range(rows):
    for j in range(column):
        
       if i == 0 or i == rows - 1 or j == 0 or j == column - 1: 
           print("*",end="")
       else:
            print(" ", end="")
    print() 
 

