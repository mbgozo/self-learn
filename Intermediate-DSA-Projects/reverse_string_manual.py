# 🎯 Objective
# Write a Python function named reverse_string_manual that takes a single string as input.
# Your function must return a new string that is the reverse of the input string.
# Constraint: You MUST NOT use Python's built-in reverse functions or slicing shortcuts (e.g., s[::-1]).
#  You must implement the reversal manually using a loop (e.g., for or while).
# 🛠️ Required Concepts
# Iteration: Using a for or while loop.
# Indexing: Accessing characters/elements by their index.
# String Concatenation (or building a list of characters and joining them).

user = input("Random text: ")
list_user = list(user)
print(list_user)
reversed_list = []

for i in list_user:
    reversed_list.insert(0,i)

final_reversed_string =  "".join(reversed_list)
print(final_reversed_string)
