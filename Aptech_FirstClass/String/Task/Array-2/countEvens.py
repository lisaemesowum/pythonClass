'''
Return the number of even ints in the given array. 
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

Examples

countEvens([2, 1, 2, 3, 4]) → 3
countEvens([2, 2, 0]) → 3
countEvens([1, 3, 5]) → 0
'''
def countEvens(nums):
    counts = 0
    for i in nums:
        if i % 2 == 0:
            counts = counts + 1
    return counts        

print(countEvens([2, 1, 2, 3, 4]))
print(countEvens([2, 2, 0]))
print(countEvens([1, 3, 5]))