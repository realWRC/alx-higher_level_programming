#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = number % 10
if result > 5:
    print(f"Last digit of {number} is {number % 10} and is greater than 5")
elif result == 0:
    print(f"Last digit of {number} is {number % 10} and is 0")
elif result < 5 and result != 0:
    print(f"Last digit of {number} is {number % 10} and is less than 6 "
          f"and not 0")
