# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

rows = 10

for a in range(rows): #number of rows
    for b in range(a + 1): #add number of rows plus 1
        print("*",end="") # print the star 
    print()#moves down.
print()    
    
    
# --------------- right aligned triangle ---------------------
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

row = 10 #means we want 10 lines
for a in range(1, row + 1):
    for b in range(a):
        print("* ", end="")
    print() #moves down.
print()    
    
# ---------- left ----------


# * * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * 
# * * * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

row = 10 #means we want 10 lines
for a in range(row, 0, - 1):
    for b in range(a):
        print("* ", end="")
    print() #moves down.
print() 
  
  
#   ----------------------- box =--------------------------
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
# * * * * * * * * * * * 
rows = 5
col = 10
for a in range(rows):
    for b in range(col, 0, - 1):
         print("* ", end="")
    print()    
print()

    
    