# pascal triangle
# write a python program to print the pascal triangle 
# trianle
#    *
#   * *
#  * * *
# * * * *
# method 1
# for i in range(0,1):
#     print("    *")
#     for j in range(0,2):
#         print( "*",end="\t")
#         for z in range(0,4):
#          print( "*",end="\n")

triangle = 10
for i in range( triangle):
    for j in range(triangle - i - 1): # print spaces to center the triangle 
        print(" ", end="") # print spaces
    for k in range(0, i + 1): # add illerate the number of stars to print in each row
        print("* ", end="")
    print()
    
    
    # anither method
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()
         
     
