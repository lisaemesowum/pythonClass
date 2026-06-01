# Task 
# create a function that will sum only the odd numbers from the users input. 
# like only take the odd numbers from the user input and sum them up.

def sum_odd_numbers():
    numbers = input("Check the odd numbers in your input (separate with space): ").split()

    total = 0

    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            print(f"{num} is an odd number.")
            total += num

    print(f"The sum of the odd numbers in your input is: {total}")

sum_odd_numbers()