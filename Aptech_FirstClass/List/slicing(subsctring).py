'''
slicing
Slicing allows you to get a portion (part) of a list, string, or tuple.

list[start:end]
➡️ Start at start
➡️ Stop before end
'''
student = ["Elana","Lisa", "Abbas", "samuel"]
# print(len(student))
print(student[0:3])
print(student[0:3][-1])
print(student[2:])
print(student[:3])

# salow coping
staff = student[:]
print(staff)