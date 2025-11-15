"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:raise ValueError("Cannot take the square root of a negative numer")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b):
    if a == 0: raise ZeroDivisionError("Cannot divide by zero!")
    return b / a

def logarithm(a, b):
    if b <= 0: raise ValueError("Cannot take the logarithm of a non-positive number!")
    return math.log(b,a)

def exponent(a, b): return a ** b