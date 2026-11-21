#use cal.py to perform calculations
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))

#different ways to import the calculator module
#1. import calculator as cal ----- ALIES METHOD
import calculator as cal
print(cal.add(10, 5))

#2. from calculator import add, subtract, multiply, divide ----- SPECIFIC FUNCTION IMPORT
from calculator import add, subtract
print(add(10, 5))
print(subtract(10, 5))

#3. from calculator import * ----- IMPORT ALL FUNCTIONS
from calculator import *
print(multiply(10, 5))


#bulid in functions
import datetime
print(datetime.date.today())

import math
print(math.sqrt(144))

import random
print(random.randint(1, 10))

import os
print(os.getcwd())


#pratice questions
#1. Import math and print: Square root of 625 , Value of pi   ,    Factorial of 5
import math
print(f"Square root of 625: {math.sqrt(625)}")
print(f"Value of pi: {math.pi}")
print(f"Factorial of 5: {math.factorial(5)}")

#2. Use random.randint() to generate five random numbers between 1 and 10
import random
randint = []
for x in range(5):
    randint.append(random.randint(1, 10))
print(f"Five random numbers between 1 and 10: {randint}")

#3. Exercise 3 — Create your own module --- calculate average marks
import average
marks = [98,34,78.8,90,67.5]
print(f"Average marks: {average.calculate_average(marks)}")

#4. Exercise 4 — Create your own module --- calculate revenue and discount
from sales_functions import calculate_total_revenue, calculate_discount
orders = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 5}]

print(f"Total revenue: {calculate_total_revenue(orders)}")
print(f"Discounted price: {calculate_discount(100, 10)}")
