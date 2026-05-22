# print("Welcome to my first class in Python!")

# number1 = 30
# number2 = 60
# sum = number1 + number2
# print("The sum of", number1, "and", number2, "is", sum)
# print(f'sum = {sum}')

# ==================input from user================
# for bank account 
# name = input("Enter your fullName? ")
# age = int(input("whats your date of birth? "))
# bank = input("which bank do you have account? ")
# bvn = input("what is your bvn? ")
# balance = float(input("what is your account balance? "))
# location = input("where do you live? ")
# nepabill = input("do you have nepa bill? ")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Bank: {bank}")
# print(f"BVN: {bvn}")
# print(f"Balance: {balance}")
# print(f"Location: {location}")
# print(f"Nepa Bill: {nepabill}")

# =====input for opay
phone_number =int(input("What is your active, accessible mobile phone number? \n"))
OTP = int(input("What is the 6-digit code sent to your phone via SMS: \n "))
personalDetails = input("What is your full name: \n")
age = int(input("whats your date of birth? \n"))
email_address = input("Enter your email address? \n")
identification = [
    "National Identity Number (NIN)",
    "BVN",
    "Voter's Card",
    "Driver's License",
    "International Passport"
]

user = input(
    "Choose an identification type: \n"
    "1. National Identity Number (NIN) \n"
    "2. BVN \n"
    "3. Voter's Card \n"
    "4. Driver's License \n"
    "5. International Passport \n"
    "Enter your choice: "
)
occupation = input(" What is your current job and annual income range: \n")
print(f"Phone Number: {phone_number} \n")
print(f"OTP: {OTP} \n")
print(f"Personal Details: {personalDetails} \n")
print(f"Age: {age} \n")
print(f"Email Address: {email_address} \n")
print("You selected: \n", identification[int(user) - 1])
print(f"Occupation: {occupation} \n")

print(phone_number,OTP,personalDetails,age,email_address,identification,occupation)