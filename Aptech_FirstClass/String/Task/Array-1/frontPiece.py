'''
Given an int array of any length, return a new array of its first 2 elements. 
If the array is smaller than length 2, use whatever elements are present.

Examples

frontPiece([1, 2, 3]) → 1,2
frontPiece([1, 2]) → 1,2
frontPiece([1]) → 1
'''
def frontPiece(nums):
    return nums[0:2]

print(frontPiece([1,2,3]))
print(frontPiece([1,2,3]))
print(frontPiece([1]))
print(frontPiece([9,8]))