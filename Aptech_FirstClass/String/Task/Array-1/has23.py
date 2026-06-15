'''
Given an int array length 2, return true if it contains a 2 or a 3.

Examples

has23([2, 5]) → true
has23([4, 3]) → true
has23([4, 5]) → false
'''
def has23(nums):
  if 2 in nums:
      return True
  if 3 in nums:
      return True
  else:
      return False
    
    
print(has23([2,5]))
print(has23([4,3]))    
print(has23([4,5]))  
print(has23([2,9]))    
  
    
