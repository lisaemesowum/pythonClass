# jumb statement are used to ulter the flow of the program. There are three jumb statement in python break, continue and pass
# python 3 jumb statement are used to ulter the flow of the program. There are three jumb statement in python 
# -------------------- break -------------------------
# break is used to exit a loop when a certain condition is met. It can be used in both for and while loops.

# --------- classwork ----------------
# write a program 1 - 6 when it reaches 3 it should break and print the value i
for i in range(1,6):
    if i == 3:
        break
    print(i)
    
    
# ---------------- continue ----------------------
# continue is used to skip the current iteration of a loop and move on to the next iteration. It can be used in both for and while loops.
for i in range(1,6):
    if i == 3:
        continue
    print(i)
    
    
# ----------------- pass ---------------------
# pass is a null statement in Python. It is used when a statement is required syntactically but no action is desired.
for i in range(1,6,2):
    pass
print("hello world")
