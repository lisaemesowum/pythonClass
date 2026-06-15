'''
Start with 2 int arrays, a and b, each length 2. 
Consider the sum of the values in each array. 
Return the array which has the largest sum. In event of a tie, return a.

Examples

biggerTwo([1, 2], [3, 4]) → 3,4
biggerTwo([3, 4], [1, 2]) → 3,4
biggerTwo([1, 1], [1, 2]) → 1,2
'''
def biggerTwo(a,b):
    # if a >= b:
    #     return a
    # else:
    #     return b
    if sum(a) >= sum(b):
        return a
    else:
        return b

print(biggerTwo([1, 2], [3, 4]))    
print(biggerTwo([3, 4], [1, 3]))
print(biggerTwo([1, 1], [1, 2]))  
print(biggerTwo([10,20],[90,30]))   
print(biggerTwo([5, 0], [1, 10]))
               