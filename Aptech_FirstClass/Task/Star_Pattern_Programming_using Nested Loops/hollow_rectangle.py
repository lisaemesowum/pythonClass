
    # ***************
    # *             *
    # *             *
    # *             *
    # ***************

# method 1 # Hollow rectangle pattern
rows = 5
column = 15

# for i in range(rows):
#     for j in range(column):
        
#        if i == 0 or i == rows - 1 or j == 0 or j == column - 1: 
#            print("*",end="")
#        else:
#             print(" ", end="")
#     print() 
 
 
   # ***************
    # *             *
    # *             *
    # *             *
    # ***************

rows = 5
column = 15

for a in range(rows):
   for b in range(column):
       if a == 0 or a == rows - 1 or b == 0 or b == column - 1: #This checks if we are on the border of the rectangle.
           print("*", end="")
       else:
          print(" ", end="")  #If not on the border, print a space.That creates the hollow middle. 
  
   print() #moves down.
