'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

Examples

rotateLeft3([1, 2, 3]) → 2,3,1
rotateLeft3([5, 11, 9]) → 11,9,5
rotateLeft3([7, 0, 0]) → 0,0,7
'''
def rotateLeft3(nums):
    n = 1
    return nums[n:] + nums[:n]  #i used slicing 

print(rotateLeft3([1,2,3]))
print(rotateLeft3([5,11,9]))
print(rotateLeft3([7,0,0]))