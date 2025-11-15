# https://github.com/runiformity173/lab11-EH-JM
# Partner 1: Eli Harrison
# Partner 2: Julissa Marcos
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math

def square_root(a):
    if a < 0:raise ValueError("Cannot take the square root of a negative numer")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a,b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b,a)

def exp(a,b):
    return a ** b

