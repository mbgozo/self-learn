# 🧮 Project Objective: The Simple Calculator
# Write a Python function that simulates a basic calculator. The program must:
# Ask the user for two distinct numbers and the mathematical operator they want to use (+, -, *, or /).
# Use if/elif/else logic to execute the correct operation.
# Include a specific conditional check to prevent the program from performing division if the second number is zero.
# If the second number is zero and the operation is division, return an error message.
# Return the final result string to be printed.

def simple_calculator():
    a,b,c = input("Enter two numbers for mathematical computation and add your operator: (Eg 2 3 +) ").split()
    A = int(a)
    B = int(b)
    if c == "+":
        return f"{A} + {B} is {A + B}"
    elif c == "-":
        return f"{A} - {B} is {A - B}"
    elif c == "*":
        return f"{A} * {B} is {A * B}"
    elif c == "/":
        if B == 0:
            return f"Error: Cant perform Arithmetics because number is 0"
        else:
            return f"{A} / {B} is {A / B}"

print(simple_calculator())