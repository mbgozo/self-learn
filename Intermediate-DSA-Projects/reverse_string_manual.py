# 🎯 Objective
# Write a Python function named reverse_string_manual that takes a single string as input.
# Your function must return a new string that is the reverse of the input string.
# Constraint: You MUST NOT use Python's built-in reverse functions or slicing shortcuts (e.g., s[::-1]).
#  You must implement the reversal manually using a loop (e.g., for or while).
# 🛠️ Required Concepts
# Iteration: Using a for or while loop.
# Indexing: Accessing characters/elements by their index.
# String Concatenation (or building a list of characters and joining them).

def reverse_string(): #function name
    user = input("Random text: ") #Takes input from User
    list_user = list(user) #Converts users input to list
    #print(list_user)
    reversed_list = [] # An empty list to be receiving iteration of the reversal

    for i in list_user: #for loop is used because the number of iterations to be completed is known(A definite data received)
        reversed_list.insert(0,i) #This inserts the accessed data at the given index in the new list and all others coming through from the iteration pushes old data to the right for new entry till iteration ends

    final_reversed_string =  "".join(reversed_list) # Combines all list items into one string with no separator
    return final_reversed_string

print(reverse_string())
