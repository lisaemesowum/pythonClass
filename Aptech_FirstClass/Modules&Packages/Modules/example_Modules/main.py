import calculator  #importing the whole calculator module
# from calculator import add, subtract #import specific functions from calculator module
from calculator import *   #import all the functions from calculator module

import config  #importing the whole config module
# ------------------- importing from ---------calculator--------------------
sum = calculator.add(12,6)
print(f"sum = {sum}")

sum = calculator.substraction(12,6)
print(f"substraction = {sum}")

sum = calculator.sumEven(10)
print(f"sum of even numbers = {sum}")

# --------------------  import the config file --------------------
print(config.APP_NAME)
print(config.VERSION)


