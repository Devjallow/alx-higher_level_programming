#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(repr(number)[-1])
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greate than 5")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
else:
    print(f"Last digit of {number} is {l_digit} and less than 6 and not 0")
