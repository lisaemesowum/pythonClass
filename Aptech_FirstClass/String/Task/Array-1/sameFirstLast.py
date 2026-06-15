'''
Given an array of ints, return true if the array is length 1 or more, and the first element and the last element are equal.

Examples

sameFirstLast([1, 2, 3]) → false
sameFirstLast([1, 2, 3, 1]) → true
sameFirstLast([1, 2, 1]) → true
'''
 
 
#  make it print true or false
def sameFirstLast(nums):
    return nums.count(1) == 2

 
print(sameFirstLast([1,2,3]))
print(sameFirstLast([1,2,3,1]))
print(sameFirstLast([1,2,1]))


