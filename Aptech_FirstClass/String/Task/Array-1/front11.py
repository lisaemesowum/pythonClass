'''
Given 2 int arrays, a and b, of any length, return a new array with the
first element of each array. If either array is length 0, ignore that array.

Examples

front11([1, 2, 3], [7, 9, 8]) → 1,7
front11([1], [2]) → 1,2
front11([1, 7], []) → 1
'''
def front11(a,b):
#    first = a[0]
#    second = b[0] 
#    return first , second
    output = []
    if len(a) > 0:
        output.append(a[0]) # If array a has items, Python grabs the first item and drops it into the box
    if len(b) > 0:
        output.append(b[0])  
    return output

print(front11([1, 2, 3], [7, 9, 8]))
print(front11([1,], [2]))
print(front11([1,7], []))