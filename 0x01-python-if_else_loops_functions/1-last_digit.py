#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if (last_digit == 0):
    last_str = "0"
elif (last_digit > 5):
    last_str = "greater than 5"
else:
    last_str = "less than 6 and not 0"
print("Last digit of {} is {} and is ".format(number, last_digit) + last_str)
