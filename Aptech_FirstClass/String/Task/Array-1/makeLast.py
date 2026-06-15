'''
Given an int array, return a new array with double the length where its last 
element is the same as the original array, and all the other elements are 0.
The original array will be length 1 or more.

Examples

makeLast([4, 5, 6]) → 0,0,0,0,0,6
makeLast([1, 2]) → 0,0,0,2
makeLast([3]) → 0,3
'''
def makeLast(nums):
    new_array = [0] * (len(nums)* 2)
    new_array[-1] = nums[-1]
    return  new_array 

print(makeLast([4,5,6]))
print(makeLast([1,2]))
print(makeLast([3]))