"""
find the second larges number 
[30,60,20,40]

"""
# number = []
# num = int(input("Length of list: "))
# for i in range(num):
#     var = int(input())
#     number.append(var)
    
# print("List: ",number)
# number.sort()

# print("Second largest number in the list: ",number[-2])


"""
Find the second largest number
"""

number = []
num = int(input("Length of list: "))
for i in range(num):
    var = int(input())
    number.append(var)
    

print("List: ",number)
number.sort()

print("Second largest number in the list:", number[-2])
