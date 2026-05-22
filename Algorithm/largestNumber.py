# Find the Largest Number

# Write a Python program that finds the largest number in a list without using max().

def largest_number(nums):
    largest = nums[0]
    
    for num in nums:
        if num > largest:
            largest = num
    return largest
numbers = [4, 8, 2, 1, 6]

print(largest_number(numbers))  
           