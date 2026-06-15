'''
Return the index of the minimum value in an array. 
The input array will have at least one element in it.

Examples

findLowestIndex([99, 98, 97, 96, 95]) → 4
findLowestIndex([2, 2, 0]) → 2
findLowestIndex([1, 3, 5]) → 0
'''
def findLowestIndex(nums):
    lowest_index = 0
    for i in range(len(nums)) :
        if nums[i] < nums[lowest_index]:
            lowest_index = i
            
    return lowest_index

print(findLowestIndex([99, 98, 97, 96, 95]))  
print(findLowestIndex([2, 2, 0]))              
print(findLowestIndex([1, 3, 5]))