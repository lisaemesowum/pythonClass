'''
We'll say that a 1 immediately followed by a 3
in an array is an "unlucky" 1. Return true if the given array contains 
an unlucky 1 in the first 2 or last 2 positions in the array.

Examples

unlucky1([1, 3, 4, 5]) → true
unlucky1([2, 1, 3, 4, 5]) → true
unlucky1([1, 1, 1]) → false

'''
def unlucky1(nums):
    if len(nums) < 2:
        return False
        
    if nums[0] == 1 and nums[1] == 3:
        return True
    if len(nums) > 2 and nums[1] == 1 and nums[2] == 3:
        return True
        
    if nums[-2] == 1 and nums[-1] == 3:
        return True
        
    return False
    
print(unlucky1([1,3,4,5])) 
print(unlucky1([2, 1, 3, 4, 5])) 
print(unlucky1([1,1,1])) 
