'''
Given an array of ints, return true if 6 appears as either the first or last 
element in the array. The array will be length 1 or more.

Examples

firstLast6([1, 2, 6]) → true
firstLast6([6, 1, 2, 3]) → true
firstLast6([13, 6, 1, 2, 3]) → false
'''
def firstLast6(nums):
    return nums[0]== 6 or nums[-1] == 6  #using the index 0 is the first index and -1 is the last index so if 6 is in index 0 true if -1 in the last
print(firstLast6([1,2,6]))
print(firstLast6([6,1,2,3]))
print(firstLast6([12,6,1,2,3]))