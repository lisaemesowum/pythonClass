# Beginner Algorithm Question
# You are given a list of numbers.
# Write a Python program to find 
# and print the duplicate numbers in the list.

def find_duplicates(nums):
    seens = set() 
    duplicates = set()

    for num in nums: #loops through list
     if num in seens: 
         duplicates.add(num)
     else:
        seens.add(num)    
    return duplicates

numbers = [1,1,4,6,7,7,7,9]
# print (find_duplicates(numbers)) 



    