#  * *   * *
# *     *     *
# *           *
#   *       *
#     *   *
#       *


rows = 6

for a in range(rows):
    for b in range(rows * 2):
        if ((a == 0 and (b == 1 or b == 2 or b == 4 or b == 5)) #top curves  * *   * *
           or(a == 1 and (b == 0 or b == 3 or b == 6)) #Creates the outer heart walls.
           or(a == 2 and (b < 7)) or(a == 3 and (b > 0 and b < 6)) 
           or (a == 4 and (b > 1 and b < 5)) or(a == 5 and b == 3) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()        
    
    
    
for i in range(6):
    for j in range(7): #Inner loop So each row has 7 column positions.
        if ((i == 0 and j % 3 != 0) or  #This works only on first row print when remainder is NOT 0
            (i == 1 and j % 3 == 0) or   #Only works on row 1.
            (i - j == 2) or             #This creates the left diagonal.This is the left slanting side.
            (i + j == 8)):              #This creates the right diagonal.
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()    