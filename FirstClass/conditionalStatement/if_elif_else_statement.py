# if elif else statement
# score = 50
# if score >= 70:
#     print("you scored an A")
# elif score >= 60:
#     print("You scored B")
# elif score >= 50:
#     print("You scored C")
# else:
#     print("you failed")
    
    # user input to check not hard coded 
course = input("Enter your course:")
if course == "python":
    print("Welcome to Aptech Python programming class, we are glad to have you here")
elif course == "Java Programming":
    print("OOps, you are in the wrong class, this is python programming class")
else:
    print("Sorry, we don't offer that course here")
    
    
    # for the score the user put in to check they grade
score = int(input("Enter your score: "))
if score >= 70:
    print("you scored an A")
elif score >= 60:
    print("You scored B")
elif score >= 50:
    print("You scored C")
else:
    print("you failed")
    
    # PRINTING THE CONSOLE
    print("|------------- Full Details -------------------------|")
    print("| Your course in Aptech",course)
    print("| Your Grade: " , score)
    print("|----------------------------------------------------|")
    
    