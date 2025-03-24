#Nico, Christopher
#Lesson 16
# Creates 100 number integers, gets the total and the average
import random
import math
import time

numbers = 100


num1 = [random.randint(1, 100) for _ in range(100)]
print(num1)
sum = sum(num1)
time.sleep(2)
print("I will now give you the average")


print("Here is the total")
print(sum)
time.sleep(1)
print("Now here is the average")
time.sleep(1)
total = sum / numbers
print(total)
