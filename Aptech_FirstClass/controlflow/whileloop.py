# while loop is used to execute a block of code repeatedly until a certain condition is met.

# ----------- while loop syntax -------------
# while condition:
#     # block of code to be executed
# example 
i = 1
while i <= 5:
    # print(i)
    i += 1
    
    # class works 
# collect the input of the user as add the number of the user unti the user enteres 0 display the sum of the numbers entered by the user

sum = 0
user = int(input("enter a number:"))
while user != 0:
    sum +=user
    user = int(input("enter a number:"))
print("The sum of the numbers entered is:", sum)

# ---------Another method --------------------
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Sum = {total}")
