#"""This is a custom python module for perfoming basic arithmetics"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
     if x != 0: return x / y
     else:
         return "Can't Perform this arithmetic"