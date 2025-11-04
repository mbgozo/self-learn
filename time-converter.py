# Write a Python script that takes a total number of minutes
# as input and converts that value into the
# equivalent number of hours and remaining minutes.
# This must be done using a function and without using any lists.

minutes = int(input("Enter your total number of minutes for conversion: "))

def convert_time(minutes):
    #Here modulo is used to deduce the remaining minutes left from the user's input
    remaining_time = minutes % 60 
    #Here floor division is used to get the number of hours from the user's input
    hour = minutes // 60
    if minutes >= 60:
        return print(f"The given {minutes} minutes is equivalent to {hour}hrs, {remaining_time}mins")
    else:
        return print(f"The given {minutes} mins does not make an hour")

convert_time(minutes)