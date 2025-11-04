# Write a Python script that takes a total number of minutes
# as input and converts that value into the
# equivalent number of hours and remaining minutes.
# This must be done using a function and without using any lists.


def convert_time():
    #Receives data from user
    minutes = int(input("Enter your total number of minutes for conversion: "))
    #Validating users entry
    if minutes < 0:
        return "ERROR: Minutes cannot be a negative number. Please try again."
    #Here modulo is used to deduce the remaining minutes left from the user's input
    remaining_time = minutes % 60 
    #Here floor division is used to get the number of hours from the user's input
    hour = minutes // 60
    return  f"The given {minutes} minutes is equivalent to {hour}hrs, {remaining_time}mins"

print(convert_time())