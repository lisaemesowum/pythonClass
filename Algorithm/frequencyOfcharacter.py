'''
count the frequency of each character in any given string
b: 1, a:3 , n:2
'''
def frequency_of_character(text):
    count : 0
    for i in text:
        count[i] = count.get(i,0) + 1
    return count
print(frequency_of_character())
