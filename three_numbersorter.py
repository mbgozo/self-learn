# Write a Python function that accepts three distinct integer numbers as input.
# Your function must use conditional logic to compare these three numbers and
# then correctly identify and print the largest number and the smallest number among the three.
def three_numbersorter():
    a, b, c = input("Enter your three distinct integer").split()
    a = int(a)
    b = int(b)
    c = int(c)
    mins = a
    maxs = a
    if maxs < b:
        maxs = b
    if maxs < c:
        maxs = c

    if mins > b:
        mins = b
    if mins > c:
        mins = c
    return f"The minimum number entered is {mins}, and the maximum is {maxs}"

print(three_numbersorter())