
# 153 => 1^3 + 5^3 + 3^ = 

# ================== check if it is armstrong or not giving ==================
 

num = input("enter your name: ")
power = len(num)
total = sum(int(digit) ** power for digit in num)
if total == int(num):
    print("yes, it is an armstrong")
else:
    print("nope")

