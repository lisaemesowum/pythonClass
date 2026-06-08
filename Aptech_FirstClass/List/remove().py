"""
.remove() method when you know the value of the item you want to delete
"""
student = ["Elana","Lisa", "Abbas", "samuel"]
result = student.remove("Lisa")
print(result)
print(student) #removes it

"""
pop()
removes and returns an item from a collection
"""
student = ["Elana","Lisa", "Abbas", "samuel"]
ass = student.pop()
print(ass)