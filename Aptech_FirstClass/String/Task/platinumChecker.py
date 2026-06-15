# a function to check if the string is a platinum or not 
def poli_checker(text):
    return text == text[::-1]
print(poli_checker("madam"))