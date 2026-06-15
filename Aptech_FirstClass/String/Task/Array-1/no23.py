'''
Given an int array length 2, return true if it does not contain a 2 or 3.

Examples

no23([4, 5]) → true
no23([4, 2]) → false
no23([3, 5]) → false
'''
def no23(nums):
   if 2 in nums or 3 in nums:
       return False
   else:
       return True
    # if 2 in nums:
    #   return False
    # if 3 in nums:
    #   return False
    # else:
    #   return True
    
print(no23([4,5]))
print(no23([4,2]))
print(no23([3,5]))