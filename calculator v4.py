import math


# Mathematical functions will be called using the arithmetic class

def add(numOne, numTwo):  # Addition of two numbers
    return numOne + numTwo


def subtract(numOne, numTwo):  # Subtraction of two numbers
    return numOne - numTwo


def multiply(numOne, numTwo):  # Multiplication of two numbers
    return numOne * numTwo


def divide(numOne, numTwo):  # Division of two numbers with error handling
    try:
        return numOne / numTwo
    except ZeroDivisionError:
        return 0


def exponent(base, exp):  # Exponent of base to a power
    return base ** exp


def factorial(numOne):  # Recursive function for factorial
    if numOne < 0:
        return 0
    elif numOne <= 1:
        return 1
    return numOne * factorial(numOne - 1)


def radians(deg):  # Degrees --> Radians
    return math.radians(deg)


def degrees(rad):  # Radians --> Degrees
    return math.degrees(rad)


def trig(angleRad, op):  # Trigonometric Operations
    if op == 'sin':
        return math.sin(angleRad)
    if op == 'cos':
        return math.cos(angleRad)
    if op == 'tan':
        return math.tan(angleRad)


def greater(numOne, numTwo):  # Boolean check if one number greater than another
    return numOne > numTwo


while True:
    operation: str = "(" + input("Please enter your mathematical operation").lower() + ")"
    if operation == "()":
        break
    else:
        steps: str[0]
        quantities: float[0]
