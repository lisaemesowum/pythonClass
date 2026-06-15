'''
Given an array of ints of odd length, look at the first, last,
and middle values in the array and return the largest.
The array length will be a least 1.

Examples

maxTriple([1, 2, 3]) → 3
maxTriple([1, 5, 3]) → 5
maxTriple([5, 2, 3]) → 5
'''
def maxTriple(nums):
    first = nums[0]
    middle = nums[len(nums) // 2]
    last = nums[-1]
    return max(first,middle,last)
   
    
  

print(maxTriple([1, 2, 3]))
print(maxTriple([1,5,3]))
print(maxTriple([5,2,3]))


    
