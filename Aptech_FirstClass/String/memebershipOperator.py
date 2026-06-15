
username = "emesowum for life"
print("eme" in username)

# STRING METHODS

print(username.upper())
print(username.lower())
print(username.title())

print(username.capitalize()) # takes the first letter to be capitalized

name = "         emesowum      "
# for removing spaces
print(name.strip())
print(len(name))

text = "i hate this"
print(text.replace("hate","love"))

# how to convert a string to a list 
words = text.split("*") #to join it to be a 
print(words)

# convert a list to a string
convert_back_string = "*".join(words)
print(text.startswith("I"))
print(text.find("love"))
# print(text.index("loveeee"))

# count how many times
print(text.count("t"))
print("lisa\nEmesowum")
print("lisa\bEmesowum")

text2 = "i love to be \"here\""
print(text2)
